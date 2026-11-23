# Chapter 02: Anatomy of an Agent Skill

## Practical exercises

### E01

Tool Registry Expansion: Add at least two new tools to the registry, including their descriptions and simulated trust scores. Test the agent skill with queries that should select the new tools.

### E02

Trust Score Dynamics: Simulate a scenario where a tool’s trust score drops due to repeated failures. How does this affect tool selection?

### E03

Adversarial Tool Injection: Add a tool with a misleading description. Observe how the agent skill handles ambiguous or adversarial tool definitions. Discuss potential defences.

### E04

Context Handling: Modify the agent to handle multi-step queries (e.g., “Calculate the sum of today’s temperature and 5”). How would you decompose and route such tasks?

### E05

Interpretability: Implement simple logging to explain why a particular tool was selected for a given query. Extend to record errors and user feedback. ---

## Review questions

### Q01

What are the essential components of an agent skill, and how do they interact?

### Q02

How does dynamic tool selection differ from static tool invocation?

### Q03

What role does the tool registry play in agent skill orchestration?

### Q04

Why is trust scoring important in tool selection, and what signals can be used?

### Q05

What are the main security risks associated with agent skills, and what defences have been proposed?

### Q06

How does the “lost-in-the-middle” effect impact agent skill performance in long-context scenarios?

### Q07

In what ways can agent skills be made more interpretable and auditable? ---

## Reference laboratories

- [Lab 02](../../labs/02/README.md)
