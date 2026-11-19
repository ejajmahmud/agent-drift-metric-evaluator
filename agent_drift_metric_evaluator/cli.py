"""CLI for Drift Evaluator."""
import argparse
from .core import DriftMetricEvaluator

def main():
    parser = argparse.ArgumentParser(description="Agent Drift Metric Evaluator CLI")
    parser.add_argument("--demo", action="store_true", help="Run drift demo")
    args = parser.parse_args()

    evaluator = DriftMetricEvaluator(drift_threshold=0.1)
    base = [0.5, 0.3, 0.2]
    shifted = [0.1, 0.2, 0.7] # major drift
    report = evaluator.compute_js_divergence(base, shifted)
    print(f"JSD: {report.jensen_shannon_div:.3f}, Has Drifted: {report.has_drifted}")

if __name__ == "__main__":
    main()
