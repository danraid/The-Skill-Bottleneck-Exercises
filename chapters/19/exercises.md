# Chapter 19: Production Operations and Continuous Evaluation

## Exercises

### E01

Instrument a Multi-Agent Workflow: Extend the lab outline to include a third agent and a new skill. Instrument all steps and visualise the execution trace.

### E02

Fault Injection: Implement systematic fault injection (e.g., random skill failures, communication drops) and evaluate the system's ability to detect and recover from faults.

### E03

Metric Computation: Compute and plot Task Success Rate, Human Intervention Rate, and Fault Detection Rate over 100 runs with varying fault probabilities.

### E04

Skill Evolution Simulation: Log failed executions and implement a simple rule to refine agent behaviour (e.g., avoid division by zero). Measure improvement in TSR.

### E05

Observability Layer Analysis: Compare the information available from operational telemetry alone versus a dual-layer (operational + reasoning) approach. Identify a failure mode detectable only with the dual-layer system. ---

## Review questions

### Q01

What are the main differences between observability in traditional ML systems and agentic AI systems?

### Q02

Describe the three-tier observability framework and explain why each tier is necessary.

### Q03

How does the "observability tax" impact production operations, and what strategies can mitigate it?

### Q04

What is the role of error budgets and autonomy contraction in Agent Operational Reliability Engineering?

### Q05

Why is skill evolution important for agentic AI, and what are the main paradigms for skill evaluation and evolution?

### Q06

How do continuous evaluation frameworks align technical performance with business outcomes?

### Q07

Give an example of a silent failure in an agentic AI system and describe how it can be detected. ---

## Reference laboratories

- [Lab 13](../../labs/13/README.md)
- [Lab 14](../../labs/14/README.md)
