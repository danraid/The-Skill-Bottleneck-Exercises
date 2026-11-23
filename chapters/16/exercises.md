# Chapter 16: Experimental Design and Architectural Ablations

## Exercises

### E01

Component Ablation: Remove the verification layer from your agent. What changes in safety and success rate do you observe? Discuss the implications for real-world deployment.

### E02

Routing Policy Swap: Implement a random routing policy that selects tools at random. Compare its performance to the baseline. What failure cases emerge?

### E03

Memory Ablation: Add a simple memory (e.g., store last tool call) and ablate it. Does it affect multi-turn queries or context-dependent tasks?

### E04

Cost Analysis: Track token usage (if using a real LLM API). How does adding verification or memory affect cost? Are there scenarios where cost increases without quality gains?

### E05

Process Evaluation: Log and analyse the sequence of actions taken by the agent. Can you identify any risky, non-compliant, or suboptimal behaviours that outcome metrics alone would miss?

### E06

Privacy Auditing: Simulate a scenario where private information must not be disclosed to certain tools. Implement trajectory-level auditing and evaluate compliance.

### E07

Reproducibility Challenge: Rerun your experiments with different random seeds or LLM sampling parameters. How stable are your results? What steps can you take to improve reproducibility? ---

## Review questions

### Q01

What is the purpose of an ablation study in agentic LLM systems?

### Q02

How does the "verifier tax" manifest in tool-using agents, and what are its implications?

### Q03

Why might multi-agent debate not outperform isolated self-correction in homogeneous teams?

### Q04

What are the main trade-offs when adding runtime guardrails to an agentic workflow?

### Q05

How can process evaluation complement outcome-based metrics in critical applications?

### Q06

Why is trajectory-level auditing necessary for privacy and security in multi-tool workflows?

### Q07

What are the limitations of LLM-as-a-judge protocols for evaluation, and how can they be mitigated? ---

## Reference laboratories

- [Lab 11](../../labs/11/README.md)
- [Lab 12](../../labs/12/README.md)
