# Chapter 11: Orchestration, Delegation, and Coordination in Multi-Agent LLM Systems

## Exercises

### E01

Delegation Chain Extension: Modify the lab code to support multi-hop delegation (e.g., Summariser delegates to Verifier for output checking). Record each step in the chain.

### E02

Failure Injection: Simulate an agent failure (e.g., Verifier returns an error). Implement fallback handling in the orchestrator.

### E03

Capability Constraints: Extend agent capabilities to include parameter-level constraints (e.g., Verifier can only check summaries under 500 words).

### E04

Auditability: Implement a function to print the full delegation chain in a human-readable format, highlighting authority boundaries.

### E05

Privacy Analysis: Identify which parts of the delegation chain and agent outputs could leak sensitive information if logged or shared. ---

## Review questions

### Q01

What are the main differences between orchestration, delegation, and coordination in multi-agent LLM systems?

### Q02

Describe the trade-offs between centralised and decentralised orchestration architectures.

### Q03

How does the CapAgent framework enforce least-privilege delegation, and why is this important?

### Q04

What are the risks of relying solely on output-level audits for privacy in multi-agent systems?

### Q05

Explain how auction-based coordination can improve decision quality in multi-agent fraud detection.

### Q06

Why do multi-agent LLM systems sometimes perform worse than solo agents, even with more exploration?

### Q07

What are the limitations of prompt-driven orchestration compared to engine-orchestrated DAGs?

### Q08

How can observability infrastructure be extended to detect agent-specific faults in orchestration pipelines? ---

## Laboratories

- [Lab 09](../../labs/09/README.md)
