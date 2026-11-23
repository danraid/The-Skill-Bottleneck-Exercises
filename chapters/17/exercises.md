# Chapter 17: Quality, Cost, Latency, and Reliability Trade-offs in Agentic AI Systems

## Exercises

### E01

Conceptual: Explain why increasing the number of agents in a workflow does not always improve quality or reliability. Support your answer with findings from recent studies.

### E02

Empirical: Modify the lab code to introduce a cost budget (e.g., max 1000 tokens per task). How does this constraint affect quality and latency?

### E03

Critical Analysis: Given a scenario where user privacy is paramount, propose architectural changes to minimise privacy over-disclosure during tool use.

### E04

Process Evaluation: Extend the lab to log each agent’s intermediate outputs. Design a compliance score to assess whether all required steps were followed.

### E05

Evaluation Design: Compare outcome-based and process-based evaluation for your workflow. What types of failures does each method reveal? ---

## Review questions

### Q01

What are the main factors that drive the trade-off between quality and cost in agentic LLM workflows?

### Q02

How does adaptive routing differ from static routing, and what are its advantages and limitations?

### Q03

Why is process evaluation important in agentic systems, especially in safety-critical domains?

### Q04

What empirical evidence suggests that memory systems can degrade reliability in agentic workflows?

### Q05

How do guardrails and runtime validation impact the latency and cost of agentic systems?

### Q06

What are the limitations of using LLMs as judges for agentic tool-calling evaluation?

### Q07

In what scenarios might a single-agent architecture be preferable to a multi-agent one? ---

## Reference laboratories

- [Lab 13](../../labs/13/README.md)
