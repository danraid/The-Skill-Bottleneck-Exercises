# Laboratory 10: Context Isolation Manager

**Learning objective:** Scope short-lived and persistent agent state safely

**Interface:** ContextStore

**Acceptance checks:** No cross-agent or cross-tenant disclosure

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
