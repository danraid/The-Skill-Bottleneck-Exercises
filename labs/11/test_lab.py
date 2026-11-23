# test_lab.py
import unittest
from main import evaluate_traces

class TestAgentEvaluationFramework(unittest.TestCase):
    def setUp(self):
        # Example traces: predicted and expected labels
        self.traces = [
            {"predicted": "A", "expected": "A"},  # correct
            {"predicted": "B", "expected": "A"},  # incorrect
            {"predicted": "C", "expected": "C"},  # correct
            {"predicted": "D", "expected": "E"},  # incorrect
            {"predicted": "E", "expected": "E"},  # correct
        ]

    def test_basic_metrics(self):
        dev_indices = {0, 1, 2}
        confirm_indices = {3, 4}
        result = evaluate_traces(self.traces, dev_indices, confirm_indices)
        self.assertEqual(result["development"]["count"], 3)
        self.assertAlmostEqual(result["development"]["accuracy"], 2/3)
        self.assertEqual(result["confirmation"]["count"], 2)
        self.assertAlmostEqual(result["confirmation"]["accuracy"], 0.5)

    def test_empty_sets(self):
        # Both sets empty
        result = evaluate_traces(self.traces, set(), set())
        self.assertEqual(result["development"], {"count": 0, "accuracy": None})
        self.assertEqual(result["confirmation"], {"count": 0, "accuracy": None})

    def test_overlap_denied(self):
        # Overlapping indices should raise
        with self.assertRaises(ValueError):
            evaluate_traces(self.traces, {0, 1}, {1, 2})

    def test_out_of_bounds_indices(self):
        # Out-of-bounds indices are ignored
        dev_indices = {0, 10, -1}
        confirm_indices = {4, 100}
        result = evaluate_traces(self.traces, dev_indices, confirm_indices)
        self.assertEqual(result["development"]["count"], 1)
        self.assertEqual(result["confirmation"]["count"], 1)
        self.assertEqual(result["development"]["accuracy"], 1.0)
        self.assertEqual(result["confirmation"]["accuracy"], 1.0)

    def test_missing_keys(self):
        # Traces missing keys are always incorrect
        traces = [
            {"predicted": "A"},
            {"expected": "A"},
            {},
        ]
        result = evaluate_traces(traces, {0, 1, 2}, set())
        self.assertEqual(result["development"]["accuracy"], 0.0)
        self.assertEqual(result["development"]["count"], 3)
        self.assertEqual(result["confirmation"], {"count": 0, "accuracy": None})

if __name__ == "__main__":
    unittest.main()

