# Laboratory 08: MCP Integration Layer

**Learning objective:** Represent tool schemas, allowlists and client/server call-contract guards without network dependency

**Interface:** MCPTool and authorised_call

**Acceptance checks:** Reject mismatched schemas and unapproved tools

## Run

Python 3.12, standard library only.

    python -m unittest -v test_lab.py

- [Reference solution source](main.py)
- [Executable tests](test_lab.py)
- [Observed original test evidence](execution.json)

Educational deterministic fixtures; does not establish LLM performance or production security.
