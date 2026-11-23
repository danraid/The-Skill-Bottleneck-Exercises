# test_lab.py
import unittest
from main import Profiler

class TestProfiler(unittest.TestCase):
    def setUp(self):
        self.prof = Profiler()

    def test_record_and_totals(self):
        self.prof.record(tokens=10, cost=0.02, latency_ms=100, model="gpt-3", success=True)
        self.prof.record(tokens=20, cost=0.03, latency_ms=200, model="gpt-3", success=False)
        self.assertEqual(self.prof.total_tokens(), 30)
        self.assertAlmostEqual(self.prof.total_cost(), 0.05)
        self.assertEqual(self.prof.count(), 2)

    def test_per_success_cost_and_p95(self):
        # 3 records: 2 successes, 1 failure
        self.prof.record(tokens=5, cost=0.01, latency_ms=50, model="gpt-4", success=True)
        self.prof.record(tokens=10, cost=0.02, latency_ms=100, model="gpt-4", success=True)
        self.prof.record(tokens=15, cost=0.03, latency_ms=200, model="gpt-4", success=False)
        # per_success_cost: (0.01+0.02)/2 = 0.015
        self.assertAlmostEqual(self.prof.per_success_cost(), 0.015)
        # p95 latency: sorted [50,100,200], 95%*3=2.85, ceil=3, idx=2
        self.assertEqual(self.prof.p95_latency(), 200)

    def test_no_success_returns_none(self):
        self.prof.record(tokens=1, cost=0.01, latency_ms=10, model="gpt-3", success=False)
        self.assertIsNone(self.prof.per_success_cost())

    def test_no_records_returns_none(self):
        self.assertIsNone(self.prof.p95_latency())
        self.assertEqual(self.prof.total_tokens(), 0)
        self.assertEqual(self.prof.total_cost(), 0.0)
        self.assertEqual(self.prof.count(), 0)

    def test_invalid_inputs(self):
        # Negative tokens
        with self.assertRaises(ValueError):
            self.prof.record(tokens=-1, cost=0.01, latency_ms=10, model="gpt-3", success=True)
        # Negative cost
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=-0.01, latency_ms=10, model="gpt-3", success=True)
        # Negative latency
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=0.01, latency_ms=-10, model="gpt-3", success=True)
        # Empty model
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=0.01, latency_ms=10, model="", success=True)
        # Non-bool success
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=0.01, latency_ms=10, model="gpt-3", success=None)
        # NaN cost
        import math
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=math.nan, latency_ms=10, model="gpt-3", success=True)
        # Inf latency
        with self.assertRaises(ValueError):
            self.prof.record(tokens=1, cost=0.01, latency_ms=math.inf, model="gpt-3", success=True)

    def test_clear(self):
        self.prof.record(tokens=1, cost=0.01, latency_ms=10, model="gpt-3", success=True)
        self.prof.clear()
        self.assertEqual(self.prof.count(), 0)
        self.assertEqual(self.prof.total_tokens(), 0)
        self.assertEqual(self.prof.total_cost(), 0.0)
        self.assertIsNone(self.prof.per_success_cost())
        self.assertIsNone(self.prof.p95_latency())

if __name__ == "__main__":
    unittest.main()

