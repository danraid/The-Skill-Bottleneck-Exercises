# Laboratory 01: Monolithic Agent

**Learning objective:** Demonstrate a single-agent skill catalogue and deterministic selection against task fixtures

**Interface:** select_skill(task, skills)

**Acceptance checks:** Select a valid skill, handle missing capabilities, log selected id

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
