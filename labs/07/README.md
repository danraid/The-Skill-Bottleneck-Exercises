# Laboratory 07: Playbook Execution Engine

**Learning objective:** Execute bounded declarative steps with checks, retries and explicit failure states

**Interface:** run_playbook(playbook,tools)

**Acceptance checks:** Preserve state transitions, prevent cycles, bounded retries

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
