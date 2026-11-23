# Chapter 10: Playbook-Driven Agent Execution

## Exercises

### E01

Playbook Extension: Modify the playbook to include a conditional branch: if the verifier rejects the answer, trigger a "refiner" agent to improve the summary and repeat the QA step.

### E02

Parallel Execution: Adapt the orchestrator to execute independent steps in parallel using Python's concurrent.futures.

### E03

Structured State: Implement a structured state object that separates ephemeral, persistent, and external data.

### E04

Failure Attribution: Instrument the orchestrator to log which agent or step fails, and suggest a remediation strategy.

### E05

Hybrid Delegation: Implement a router that chooses between structured and natural language delegation for each step, inspired by Routed Graph Handoff .

### E06

Automated Playbook Synthesis: Write a function that takes a natural language task description and generates a playbook DAG, mapping subtasks to available agents.

### E07

Security Layer: Integrate capability-based delegation into the orchestrator, ensuring that each agent invocation is authorised according to least-privilege principles. ---

## Review questions

### Q01

What are the main advantages of playbook-driven agent execution over prompted orchestration?

### Q02

How does explicit memory architecture contribute to reliability and performance in agentic systems?

### Q03

What are the trade-offs between deterministic and dynamic orchestration in multi-agent workflows?

### Q04

How do playbook-driven systems address tool-use hallucination and failure attribution?

### Q05

What security and privacy risks are introduced by centralised orchestrators, and how can they be mitigated?

### Q06

How does evidence-driven execution improve robustness in multi-agent workflows?

### Q07

What are the challenges of automated playbook synthesis and modularisation?

### Q08

How can hybrid orchestration models balance flexibility and reproducibility? ---

## Laboratories

- [Lab 07](../../labs/07/README.md)
