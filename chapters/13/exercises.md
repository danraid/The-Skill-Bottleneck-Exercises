# Chapter 13: Agent Memory and State Isolation

## Exercises

### E01

Memory Poisoning Simulation: Extend the lab to simulate a memory poisoning attack (e.g., insert a malicious entry) and implement a detection mechanism based on provenance or trust score. Discuss the limitations of trust scoring as a sole defence.

### E02

Provenance Query: Add a method to retrieve all memory entries created by a specific provenance source. Use this to analyse the influence of different sources on agent behaviour.

### E03

Audit Trail Analysis: Write a script to analyse the audit log and detect suspicious patterns (e.g., rapid trust score drops, repeated updates from a single provenance).

### E04

Multi-Agent Scenario: Instantiate two agents and demonstrate that memory entries are not shared between them. Attempt to access another agent’s memory and document the result.

### E05

GDPR Erasure: Implement a method to delete all memory and audit log entries associated with a given user or provenance. Discuss the implications for compliance and operational integrity.

### E06

Formal Belief Revision Exercise: Sketch an algorithm for belief revision in a simplified property graph. Given a conflicting new fact, identify which existing beliefs must be retracted to maintain consistency.

### E07

Zero-Trust Boundary Simulation: Modify the lab to require authentication tokens for all memory operations. Demonstrate how missing or invalid tokens prevent unauthorised access. ---

## Review questions

### Q01

What are the main architectural patterns for agent memory, and how do they differ in terms of privacy and scalability?

### Q02

Why is state isolation critical in multi-agent and multi-tenant environments?

### Q03

Describe the main security risks associated with agent memory, particularly in MCP-based systems.

### Q04

How does provenance metadata support both security and governance in agent memory architectures?

### Q05

What are the trade-offs between local-first and cloud-native memory systems for agents?

### Q06

How can formal belief revision frameworks improve the reliability of agent memory updates?

### Q07

What governance controls are necessary to ensure safe and auditable agent memory use in enterprise settings?

### Q08

Give an example of a supply-chain attack in the context of agent memory and describe how it could be mitigated.

### Q09

Discuss the limitations of Bayesian trust scoring as a defence against memory poisoning.

### Q10

Explain how audit trails and provenance queries can be used to support GDPR-compliant erasure. ---

## Reference laboratories

- [Lab 10](../../labs/10/README.md)
