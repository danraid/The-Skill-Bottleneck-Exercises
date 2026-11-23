# Chapter 13: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Memory Poisoning Simulation: Extend the lab to simulate a memory poisoning attack (e.g., insert

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Memory Poisoning Simulation: Insert a malicious entry and implement detection based on low trust score or suspicious provenance. - Cross-Agent Isolation Check: Instantiate multiple agents and verify that their memories are strictly separated. - Provenance Query: Retrieve all entries from a given provenance. - GDPR Erasure: Delete all entries and logs associated with a specific user or provenance. - Agent class: Each instance has its own SQLite database. - Memory entry: Stores content, timestamp, provenance, and trust score. - Trust scoring: Simple Bayesian update based on feedback (e.g., user marks entry as valid/invalid). - Isolation: No cross-agent memory access. - Audit log: Records all memory operations.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E02: Provenance Query: Add a method to retrieve all memory entries created by a specific provenance 

**Suggested implementation:** Distinguish persistent versus session state, isolate tenants and agents, then measure retrieval quality and failure propagation.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Agent Initialisation: Each agent instance creates its own SQLite database file, ensuring per-agent isolation. 2. Memory Insertion: When a new memory is added, it is stored with content, timestamp, provenance, and an initial trust score. 3. Trust Update: User feedback (valid/invalid) triggers a Bayesian update to the trust score. 4. Memory Retrieval: Query memories by content, returning entries sorted or filtered by trust score. 5. Au A provenance query might retrieve all memory entries created by a specific user or tool, enabling targeted review or erasure (e.g., for GDPR compliance).

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E03: Audit Trail Analysis: Write a script to analyse the audit log and detect suspicious patterns (e

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Bayesian trust scoring and provenance tracking can help identify and demote suspicious entries. - Multi-layered validation: Static metadata analysis, behavioural anomaly detection, and user transparency mechanisms . - Runtime defence systems: Proxies such as SHIELDMCP perform pre-call description integrity checks, outbound parameter sanitisation, and post-response analysis . - Agent class: Each instance has its own SQLite database. - Memory entry: Stores content, timestamp, provenance, and trust score. - Trust scoring: Simple Bayesian update based on feedback (e.g., user marks entry as valid/invalid). - Isolation: No cross-agent memory access. - Audit log: Records all memory operations.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E04: Multi-Agent Scenario: Instantiate two agents and demonstrate that memory entries are not shared

**Suggested implementation:** Distinguish persistent versus session state, isolate tenants and agents, then measure retrieval quality and failure propagation.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Agentic AI: Autonomous systems, often LLM-based, capable of planning, tool use, and collaboration . - Memory (in agents): Persistent or ephemeral storage of context, facts, or experiences that inform agent reasoning and behaviour . - State Isolation: Architectural and operational measures to prevent unintended sharing or leakage of agent state (including memory) across tasks, users, or agents . - Model Context Protocol (MCP): An open  State isolation—the separation of agent memory and execution context—emerges as a critical architectural and governance concern. Without robust isolation, agents may leak sensitive data, inherit unauthorised privileges, or become vectors for supply-chain attacks ; . These risks are amplified in multi-agent and multi-tenant environments, where shared resources and composable workflows are common.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E05: GDPR Erasure: Implement a method to delete all memory and audit log entries associated with a g

**Suggested implementation:** Distinguish persistent versus session state, isolate tenants and agents, then measure retrieval quality and failure propagation.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Agent Initialisation: Each agent instance creates its own SQLite database file, ensuring per-agent isolation. 2. Memory Insertion: When a new memory is added, it is stored with content, timestamp, provenance, and an initial trust score. 3. Trust Update: User feedback (valid/invalid) triggers a Bayesian update to the trust score. 4. Memory Retrieval: Query memories by content, returning entries sorted or filtered by trust score. 5. Au - Memory Poisoning Simulation: Insert a malicious entry and implement detection based on low trust score or suspicious provenance. - Cross-Agent Isolation Check: Instantiate multiple agents and verify that their memories are strictly separated. - Provenance Query: Retrieve all entries from a given provenance. - GDPR Erasure: Delete all entries and logs associated with a specific user or provenance.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E06: Formal Belief Revision Exercise: Sketch an algorithm for belief revision in a simplified proper

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Receive new information (possibly conflicting with existing beliefs). 2. Identify minimal inconsistent subsets of the current belief base. 3. Retract or revise beliefs to restore consistency, prioritising relevance and provenance. 4. Update provenance chains to reflect the revision history. Kumiho represents a graph-native cognitive memory architecture grounded in formal belief revision semantics . Rather than treating memory as a flat or sequential store, Kumiho models knowledge as a property graph, where nodes represent facts or beliefs and edges capture dependencies, provenance, and versioning.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

### E07: Zero-Trust Boundary Simulation: Modify the lab to require authentication tokens for all memory 

**Suggested implementation:** Distinguish persistent versus session state, isolate tenants and agents, then measure retrieval quality and failure propagation.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Agentic AI: Autonomous systems, often LLM-based, capable of planning, tool use, and collaboration . - Memory (in agents): Persistent or ephemeral storage of context, facts, or experiences that inform agent reasoning and behaviour . - State Isolation: Architectural and operational measures to prevent unintended sharing or leakage of agent state (including memory) across tasks, users, or agents . - Model Context Protocol (MCP): An open  - Agent class: Each instance has its own SQLite database. - Memory entry: Stores content, timestamp, provenance, and trust score. - Trust scoring: Simple Bayesian update based on feedback (e.g., user marks entry as valid/invalid). - Isolation: No cross-agent memory access. - Audit log: Records all memory operations.

**Source-code reference:** [Lab 10](../../labs/10/README.md).

## Review-question answers

### Q01: What are the main architectural patterns for agent memory, and how do they differ in terms of p

**Model answer:** 1. Define the roles and challenges of memory in agentic AI systems, especially those built on large language models (LLMs). 2. Explain the architectural patterns for agent memory, including retrieval-augmented, graph-native, and privacy-preserving designs. 3. Describe the security and governance risks associated with agent memory and state sharing, including memory poisoning and supply-chain attacks. 4. Evaluate trade-offs between memor Agent memory is not a monolith; it encompasses a spectrum of architectural patterns, each with distinct trade-offs in privacy, scalability, explainability, and resilience. This section explores the leading paradigms, their operational mechanics, and their suitability for different deployment scenarios.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: Why is state isolation critical in multi-agent and multi-tenant environments?

**Model answer:** State isolation—the separation of agent memory and execution context—emerges as a critical architectural and governance concern. Without robust isolation, agents may leak sensitive data, inherit unauthorised privileges, or become vectors for supply-chain attacks ; . These risks are amplified in multi-agent and multi-tenant environments, where shared resources and composable workflows are common. Without strict isolation, agents may inadvertently leak sensitive state (e.g., user data, credentials) or inherit privileges beyond their intended scope . This is exacerbated in multi-tenant or multi-agent deployments, where shared memory or credentials can become vectors for lateral movement .

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: Describe the main security risks associated with agent memory, particularly in MCP-based system

**Model answer:** 1. Define the roles and challenges of memory in agentic AI systems, especially those built on large language models (LLMs). 2. Explain the architectural patterns for agent memory, including retrieval-augmented, graph-native, and privacy-preserving designs. 3. Describe the security and governance risks associated with agent memory and state sharing, including memory poisoning and supply-chain attacks. 4. Evaluate trade-offs between memor Agentic AI systems—particularly those powered by large language models—are rapidly evolving from stateless assistants into autonomous, tool-using, and collaborative agents . This transformation introduces new requirements for memory: agents must recall prior interactions, persist knowledge across sessions, and coordinate with other agents or external tools. However, as memory becomes richer and more persistent, so do the risks: privacy 

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: How does provenance metadata support both security and governance in agent memory architectures

**Model answer:** - Scalability: Local-first memory systems may struggle with large-scale, distributed deployments or collaborative workflows . Synchronising isolated memories without introducing leakage or performance bottlenecks remains an open challenge. - Schema Evolution: Updating memory schemas or consolidating long-term memories is difficult, especially in multimodal or evolving domains . Backwards compatibility and migration tools are often lacki 1. Define the roles and challenges of memory in agentic AI systems, especially those built on large language models (LLMs). 2. Explain the architectural patterns for agent memory, including retrieval-augmented, graph-native, and privacy-preserving designs. 3. Describe the security and governance risks associated with agent memory and state sharing, including memory poisoning and supply-chain attacks. 4. Evaluate trade-offs between memor

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: What are the trade-offs between local-first and cloud-native memory systems for agents?

**Model answer:** 1. Define the roles and challenges of memory in agentic AI systems, especially those built on large language models (LLMs). 2. Explain the architectural patterns for agent memory, including retrieval-augmented, graph-native, and privacy-preserving designs. 3. Describe the security and governance risks associated with agent memory and state sharing, including memory poisoning and supply-chain attacks. 4. Evaluate trade-offs between memor | Dimension | Local-First Memory | Cloud-Native Shared Memory | Graph-Native Cognitive Memory | |------------------------|---------------------------------------|----------------------------------------|----------------------------------------| | Privacy | High (data stays local) | Lower (centralised attack surface) | Variable (depends on deployment) | | Scalability | Limited by local resources | High (cloud elasticity) | Moderate (grap

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: How can formal belief revision frameworks improve the reliability of agent memory updates?

**Model answer:** Graph-native memory architectures can leverage formal belief revision frameworks (e.g., AGM postulates) to ensure rational and explainable updates to agent knowledge . - Agentic AI: Autonomous systems, often LLM-based, capable of planning, tool use, and collaboration . - Memory (in agents): Persistent or ephemeral storage of context, facts, or experiences that inform agent reasoning and behaviour . - State Isolation: Architectural and operational measures to prevent unintended sharing or leakage of agent state (including memory) across tasks, users, or agents . - Model Context Protocol (MCP): An open 

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q07: What governance controls are necessary to ensure safe and auditable agent memory use in enterpr

**Model answer:** This chapter surveys the landscape of agent memory and state isolation, drawing on recent research and enterprise deployments. We examine architectural patterns, security threats, governance frameworks, and practical implementation strategies. Throughout, we emphasise the interplay between technical controls and organisational governance, highlighting the need for both to ensure safe, reliable, and explainable agentic AI. Agent memory and state isolation are foundational to the safe, reliable, and explainable operation of agentic AI systems. Architectural choices—ranging from retrieval-augmented and graph-native memory to privacy-preserving local-first designs—must be balanced against security, scalability, and governance needs. As protocols like MCP enable richer tool and memory integration, robust isolation, provenance, and auditability become non-nego

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q08: Give an example of a supply-chain attack in the context of agent memory and describe how it cou

**Model answer:** 1. Define the roles and challenges of memory in agentic AI systems, especially those built on large language models (LLMs). 2. Explain the architectural patterns for agent memory, including retrieval-augmented, graph-native, and privacy-preserving designs. 3. Describe the security and governance risks associated with agent memory and state sharing, including memory poisoning and supply-chain attacks. 4. Evaluate trade-offs between memor State isolation—the separation of agent memory and execution context—emerges as a critical architectural and governance concern. Without robust isolation, agents may leak sensitive data, inherit unauthorised privileges, or become vectors for supply-chain attacks ; . These risks are amplified in multi-agent and multi-tenant environments, where shared resources and composable workflows are common.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q09: Discuss the limitations of Bayesian trust scoring as a defence against memory poisoning.

**Model answer:** - SQLite-backed storage with full-text search for efficient local retrieval. - Knowledge graph clustering for semantic organisation of memories. - Event-driven coordination with per-agent provenance tracking. - Bayesian trust scoring to defend against memory poisoning. - Adaptive re-ranking to personalise retrieval and mitigate poisoned entries. Limitation: Bayesian trust scoring alone is insufficient against sophisticated, coordinated poisoning campaigns. Complementary defences—such as provenance validation, anomaly detection, and human-in-the-loop review—are necessary for robust protection.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q10: Explain how audit trails and provenance queries can be used to support GDPR-compliant erasure. 

**Model answer:** SuperLocalMemory supports GDPR-compliant erasure by isolating behavioural data in a separate database, allowing one-command deletion of all entries associated with a given user or provenance. 1. Agent Initialisation: Each agent instance creates its own SQLite database file, ensuring per-agent isolation. 2. Memory Insertion: When a new memory is added, it is stored with content, timestamp, provenance, and an initial trust score. 3. Trust Update: User feedback (valid/invalid) triggers a Bayesian update to the trust score. 4. Memory Retrieval: Query memories by content, returning entries sorted or filtered by trust score. 5. Au

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
