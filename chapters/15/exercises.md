# Chapter 15: Building a Skill Scalability Benchmark

## Exercises

### E01

Design a Multi-Step Task: Create a synthetic task that requires at least three distinct skills (e.g., retrieval, reasoning, tool use). Implement a workflow and log each step.

### E02

Process Evaluation: Extend the lab to record and score compliance with a prescribed process. Analyse cases where the agent skips steps or takes shortcuts.

### E03

Cost-Quality Trade-off: Vary the number of workflow steps and measure how token usage and latency scale with task complexity. Plot the trade-off curve.

### E04

Memory Evaluation: Simulate a multi-session agent that must recall information from previous sessions. Introduce memory errors and measure their impact on downstream task success.

### E05

LLM-as-Judge Calibration: Implement a simple LLM-as-judge protocol and compare its decisions to human labels on a subset of outputs. Analyse agreement and identify structural ceilings. ---

## Review questions

### Q01

What are the main challenges in benchmarking skill scalability for agentic LLM systems?

### Q02

How does process evaluation differ from traditional outcome-based evaluation, and why is it important?

### Q03

Describe two methods for balancing cost and quality in multi-agent workflows.

### Q04

What are the risks of relying solely on LLM-as-judge evaluation, and how can they be mitigated?

### Q05

How does memory reliability affect skill scalability in long-horizon tasks?

### Q06

Why is trajectory-level auditing necessary for privacy and safety in tool-using agents? ---

## Reference laboratories

- [Lab 11](../../labs/11/README.md)
- [Lab 12](../../labs/12/README.md)
