# main.py
from typing import List, Dict, Optional
import threading
import math

class Profiler:
    def __init__(self):
        self._lock = threading.Lock()
        self._records: List[Dict] = []

    def record(self, *, tokens: int, cost: float, latency_ms: float, model: str, success: bool):
        """
        Record a single model call.
        Args:
            tokens (int): Number of tokens used (>=0)
            cost (float): Cost in USD (>=0)
            latency_ms (float): Latency in milliseconds (>=0)
            model (str): Model name (non-empty string)
            success (bool): Whether the call succeeded
        Raises:
            ValueError: On invalid input
        """
        if not isinstance(tokens, int) or tokens < 0:
            raise ValueError("Invalid tokens: must be non-negative integer")
        if not isinstance(cost, (float, int)) or cost < 0 or math.isnan(cost) or math.isinf(cost):
            raise ValueError("Invalid cost: must be non-negative finite float")
        if not isinstance(latency_ms, (float, int)) or latency_ms < 0 or math.isnan(latency_ms) or math.isinf(latency_ms):
            raise ValueError("Invalid latency: must be non-negative finite float")
        if not isinstance(model, str) or not model:
            raise ValueError("Invalid model: must be non-empty string")
        if not isinstance(success, bool):
            raise ValueError("Invalid success: must be bool")
        rec = {
            "tokens": tokens,
            "cost": float(cost),
            "latency_ms": float(latency_ms),
            "model": model,
            "success": success
        }
        with self._lock:
            self._records.append(rec)

    def per_success_cost(self) -> Optional[float]:
        """
        Returns average cost per successful call, or None if no successes.
        """
        with self._lock:
            successes = [r["cost"] for r in self._records if r["success"]]
        if not successes:
            return None
        return sum(successes) / len(successes)

    def p95_latency(self) -> Optional[float]:
        """
        Returns the 95th percentile latency (ms) over all records, or None if no records.
        """
        with self._lock:
            latencies = sorted(r["latency_ms"] for r in self._records)
        n = len(latencies)
        if n == 0:
            return None
        idx = math.ceil(0.95 * n) - 1
        idx = min(max(idx, 0), n - 1)
        return latencies[idx]

    def total_tokens(self) -> int:
        with self._lock:
            return sum(r["tokens"] for r in self._records)

    def total_cost(self) -> float:
        with self._lock:
            return sum(r["cost"] for r in self._records)

    def count(self) -> int:
        with self._lock:
            return len(self._records)

    def clear(self):
        with self._lock:
            self._records.clear()

