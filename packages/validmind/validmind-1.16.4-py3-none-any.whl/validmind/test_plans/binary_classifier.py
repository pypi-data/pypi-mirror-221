# This software is proprietary and confidential. Unauthorized copying,
# modification, distribution or use of this software is strictly prohibited.
# Please refer to the LICENSE file in the root directory of this repository
# for more information.
#
# Copyright © 2023 ValidMind Inc. All rights reserved.

"""
Test plan for sklearn classifier models

Ideal setup is to have the API client to read a
custom test plan from the project's configuration
"""

from validmind.vm_models import TestPlan


class BinaryClassifierMetrics(TestPlan):
    """
    Test plan for sklearn classifier metrics
    """

    name = "binary_classifier_metrics"
    required_context = ["model"]
    tests = [
        "validmind.model_validation.ModelMetadata",
        "validmind.data_validation.DatasetSplit",
        "validmind.model_validation.sklearn.ConfusionMatrix",
        "validmind.model_validation.sklearn.ClassifierInSamplePerformance",
        "validmind.model_validation.sklearn.ClassifierOutOfSamplePerformance",
        "validmind.model_validation.sklearn.PermutationFeatureImportance",
        "validmind.model_validation.sklearn.PrecisionRecallCurve",
        "validmind.model_validation.sklearn.ROCCurve",
        "validmind.model_validation.sklearn.PopulationStabilityIndex",
        "validmind.model_validation.sklearn.SHAPGlobalImportance",
    ]


class BinaryClassifierPerformance(TestPlan):
    """
    Test plan for sklearn classifier models
    """

    name = "binary_classifier_validation"
    required_context = ["model"]
    tests = [
        "validmind.model_validation.sklearn.MinimumAccuracy",
        "validmind.model_validation.sklearn.MinimumF1Score",
        "validmind.model_validation.sklearn.MinimumROCAUCScore",
        "validmind.model_validation.sklearn.TrainingTestDegradation",
    ]


class BinaryClassifierDiagnosis(TestPlan):
    """
    Test plan for sklearn classifier model diagnosis tests
    """

    name = "binary_classifier_model_diagnosis"
    required_context = ["model"]
    tests = [
        "validmind.model_validation.sklearn.OverfitDiagnosis",
        "validmind.model_validation.sklearn.WeakspotsDiagnosis",
        "validmind.model_validation.sklearn.RobustnessDiagnosis",
    ]
