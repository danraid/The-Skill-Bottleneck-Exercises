# Laboratory 03: Semantic Skill Router

**Learning objective:** Rank similar skill descriptions under configurable top-k and domain constraints

**Interface:** route(query, skills, k)

**Acceptance checks:** Stable top-k, no out-of-domain leakage, deterministic tie-breaking

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
