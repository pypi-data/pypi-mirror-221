# This software is proprietary and confidential. Unauthorized copying,
# modification, distribution or use of this software is strictly prohibited.
# Please refer to the LICENSE file in the root directory of this repository
# for more information.
#
# Copyright © 2023 ValidMind Inc. All rights reserved.

"""
A TestSuite is a collection of TestPlans. It is a helpful way to organize
TestPlans that are related to each other. For example, a TestSuite could be
created for a specific use case or model methodology, to run a colllection
of plans for data validation and model validation with a single function call.
"""

from dataclasses import dataclass
from typing import ClassVar, List, Union

import ipywidgets as widgets
from IPython.display import display

from ..test_plans import get_by_id as get_test_plan
from ..utils import is_notebook
from .test_context import TestContext
from .test_plan import TestPlan


@dataclass
class TestSuite(TestPlan):
    """
    Base class for test suites. Test suites are used to define any
    arbitrary grouping of test plans that will be run on a dataset and/or model.
    """

    # stores the test plan names or classes depending on how the suite is initialized
    test_plans: ClassVar[List[Union[str, TestPlan]]] = None
    # stores the test plan classes
    _test_plan_classes: List[TestPlan] = None
    # Stores a reference to the child test plan instances
    # so we can access their results after running the test suite
    _test_plan_instances: List[object] = None

    # ipywidgets progress bar
    pbar: widgets.IntProgress = None
    pbar_description: widgets.Label = None
    pbar_box: widgets.HBox = None
    _total_tests: int = 0

    def __post_init__(self):
        if self.test_context is None:
            self.test_context = TestContext(
                dataset=self.dataset,
                model=self.model,
                models=self.models,
            )

        self._test_plan_classes = []
        for test_plan_id_or_class in self.test_plans:
            if isinstance(test_plan_id_or_class, str):
                test_plan_class = get_test_plan(test_plan_id_or_class)
            else:
                test_plan_class = test_plan_id_or_class

            self._test_plan_classes.append(test_plan_class)
            self._total_tests += len(test_plan_class.tests)

    def _init_pbar(self, send: bool = True):
        """
        Initializes the progress bar elements
        """
        self.pbar = widgets.IntProgress(
            value=0,
            min=0,
            max=self._total_tests * 2 if send else self._total_tests,
            step=1,
            bar_style="",
            orientation="horizontal",
        )
        self.pbar_description = widgets.Label(value="Running test suite...")
        # Display them in a horizontal box
        self.pbar_box = widgets.HBox([self.pbar_description, self.pbar])

        display(self.pbar_box)

    def run(self, send=True):
        """
        Runs the test suite.
        """
        self._init_pbar(send=send)

        self._test_plan_instances = []
        for test_plan_class in self._test_plan_classes:
            test_plan = test_plan_class(
                config=self.config,
                test_context=self.test_context,
                pbar=self.pbar,
                pbar_description=self.pbar_description,
                pbar_box=self.pbar_box,
            )
            self._test_plan_instances.append(test_plan)

        for test_plan in self._test_plan_instances:
            test_plan.run(render_summary=False, send=send)

        self.summarize()
        self.pbar_description.value = "Test suite complete!"

    def _results_title(self) -> str:
        """
        Builds the title for the results of the test plan
        """
        return f'<h2>Test Suite Results: <i style="color: #DE257E">{self.title()}</i></h2><hr>'

    def _results_summary(self) -> str:
        """
        Builds a summary of the results for each of the test plans in the test suite.
        This makes use of the readily available HTML summary of the test plan.
        """
        accordions = []
        for result in self._test_plan_instances:
            accordions.append(result.summary)

        return accordions

    def summarize(self):
        """
        Summarizes the results of the test suite.
        """
        # avoid circular import
        from ..api_client import get_api_host, get_api_project

        if not is_notebook():
            return

        if len(self._test_plan_instances) == 0:
            return

        title = widgets.HTML(value=self._results_title())
        ui_host = get_api_host().replace("/api/v1/tracking", "").replace("api", "app")
        results_link = widgets.HTML(
            value=f'<h3>Check out the updated documentation in your <a href="{ui_host}/projects/{get_api_project()}/project-overview" target="_blank">ValidMind project</a>.</h3>'
        )

        accordion_contents = self._results_summary()
        accordion_widget = widgets.Accordion(children=accordion_contents)
        for i, _ in enumerate(accordion_widget.children):
            accordion_widget.set_title(
                i,
                f"Test Plan: {self._test_plan_instances[i].title()} ({self._test_plan_instances[i].name})",
            )

        style_footer = widgets.HTML(
            value="""
        <style>
            .result {
                margin: 10px 0;
                padding: 10px;
                background-color: #f1f1f1;
                border: 1px solid #ccc;
                border-radius: 5px;
            }
        </style>
        """
        )

        html = widgets.VBox([title, results_link, accordion_widget, style_footer])
        display(html)

    @property
    def results(self):
        """
        Returns the results of the test suite.
        """
        return [test_plan.results for test_plan in self._test_plan_instances]
