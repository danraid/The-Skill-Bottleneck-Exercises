# main.py
"""
Agent Evaluation Framework (Educational Prototype)

Implements evaluate_traces(traces: list[dict], dev_indices: set[int], confirm_indices: set[int]) -> dict

- traces: list of dicts, each representing a trace with at least 'predicted' and 'expected' keys
- dev_indices: set of indices for development set
- confirm_indices: set of indices for confirmation set

Returns a dict with explicit metrics for both sets, without leaking labels across sets.
"""
from typing import List, Dict, Set

def _compute_metrics(traces: List[dict], indices: Set[int]) -> dict:
    """Compute accuracy and counts for a subset of traces."""
    total = len(indices)
    if total == 0:
        return {"count": 0, "accuracy": None}
    correct = 0
    for idx in indices:
        trace = traces[idx]
        # Defensive: missing keys are treated as incorrect
        if 'predicted' in trace and 'expected' in trace:
            if trace['predicted'] == trace['expected']:
                correct += 1
    accuracy = correct / total if total > 0 else None
    return {"count": total, "accuracy": accuracy}

def evaluate_traces(
    traces: List[Dict],
    dev_indices: Set[int],
    confirm_indices: Set[int]
) -> Dict:
    """
    Evaluate traces on dev and confirmation sets, returning explicit metrics.
    No leakage: metrics for each set are computed only from their own indices.
    """
    n = len(traces)
    # Defensive: Only allow valid indices
    dev_indices = {i for i in dev_indices if 0 <= i < n}
    confirm_indices = {i for i in confirm_indices if 0 <= i < n}
    # Prohibit overlap
    if dev_indices & confirm_indices:
        raise ValueError("Development and confirmation sets must not overlap.")
    dev_metrics = _compute_metrics(traces, dev_indices)
    confirm_metrics = _compute_metrics(traces, confirm_indices)
    return {
        "development": dev_metrics,
        "confirmation": confirm_metrics
    }

