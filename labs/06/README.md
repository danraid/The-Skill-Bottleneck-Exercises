# Laboratory 06: Custom Subagent Factory

**Learning objective:** Instantiate immutable specialist profiles with constrained tool permissions

**Interface:** SubagentProfile and factory

**Acceptance checks:** Validate profile, deny unauthorized tools, isolate instances

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
