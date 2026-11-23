# Laboratory 13: Cost and Latency Profiler

**Learning objective:** Attribute token usage, billed model calls and per-task latencies

**Interface:** Profiler

**Acceptance checks:** Reject invalid costs, compute per-success cost and p95 correctly

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
