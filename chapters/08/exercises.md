# Chapter 08: From Monolithic Agents to Specialised Subagents

## Exercises

### E01

Role Expansion: Add a Compliance subagent that checks whether retrieved information adheres to a given policy.

### E02

Failure Simulation: Inject a failure into the Retriever and implement fallback handling in the Orchestrator.

### E03

Memory Analysis: Modify the MemoryBank to support section-level evidence storage as in ADORE .

### E04

Coordination Cost Measurement: Measure the number of messages and steps required in both monolithic and multi-agent modes for a complex query.

### E05

Security Extension: Implement a simple capability chain for delegation and verify that only authorised agents can perform certain actions . ---

## Review questions

### Q01

What are the main limitations of monolithic LLM agents in complex, real-world tasks?

### Q02

How does explicit task decomposition into specialised subagents improve modularity and traceability?

### Q03

What are the trade-offs between natural language and structured graph-based communication in multi-agent systems?

### Q04

Describe one coordination mechanism that can be used to resolve conflicting recommendations among subagents.

### Q05

What security and privacy risks are unique to multi-agent LLM systems compared to monolithic agents?

### Q06

How can failure attribution be improved in multi-agent orchestration frameworks?

### Q07

Explain the concept of the autonomy paradox in ethical multi-agent coordination. ---

## Laboratories

- [Lab 06](../../labs/06/README.md)
