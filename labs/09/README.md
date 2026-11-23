# Laboratory 09: Hierarchical Orchestrator

**Learning objective:** Assign tasks to domain subagents and collect structured outcomes

**Interface:** dispatch(task,profiles)

**Acceptance checks:** Correct domain delegation, no cyclic delegation

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
