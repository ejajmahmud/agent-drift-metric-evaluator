"""Tests for Drift Evaluator."""
import unittest
from agent_drift_metric_evaluator.core import DriftMetricEvaluator

class TestDriftMetricEvaluator(unittest.TestCase):
    def test_identical_distributions_have_zero_drift(self):
        e = DriftMetricEvaluator(drift_threshold=0.05)
        d = [0.4, 0.4, 0.2]
        r = e.compute_js_divergence(d, d)
        self.assertAlmostEqual(r.jensen_shannon_div, 0.0)
        self.assertFalse(r.has_drifted)
