# Laboratory 11: Agent Evaluation Framework

**Learning objective:** Evaluate recorded traces independently from expected labels and prohibit leakage

**Interface:** evaluate_traces

**Acceptance checks:** Separate development/confirmation sets, return explicit metrics

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
