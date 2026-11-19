"""Core Drift Metric Evaluator."""
from typing import List, Dict
import math

class DriftReport:
    def __init__(self, jensen_shannon_div: float, has_drifted: bool):
        self.jensen_shannon_div = jensen_shannon_div
        self.has_drifted = has_drifted

class DriftMetricEvaluator:
    def __init__(self, drift_threshold: float = 0.2):
        self.drift_threshold = drift_threshold

    @staticmethod
    def _kl_divergence(p: List[float], q: List[float]) -> float:
        kl = 0.0
        for pi, qi in zip(p, q):
            if pi > 0 and qi > 0:
                kl += pi * math.log2(pi / qi)
        return kl

    def compute_js_divergence(self, p_dist: List[float], q_dist: List[float]) -> DriftReport:
        # Normalize distributions
        sum_p = sum(p_dist) or 1.0
        sum_q = sum(q_dist) or 1.0
        p = [x / sum_p for x in p_dist]
        q = [x / sum_q for x in q_dist]

        m = [(pi + qi) / 2.0 for pi, qi in zip(p, q)]
        jsd = 0.5 * self._kl_divergence(p, m) + 0.5 * self._kl_divergence(q, m)
        has_drifted = jsd > self.drift_threshold
        return DriftReport(jensen_shannon_div=jsd, has_drifted=has_drifted)
