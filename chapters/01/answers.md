# Chapter 01: Worked Answers

The reference responses are based on the corresponding chapter. Open-ended assignments can admit multiple correct designs.

## Exercise solutions

### E01: Extend the Tool Registry: Add multiplication and division tools. Update the intent classifier a

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Add multiplication and division tools. - Implement trust decay for recent failures. - Simulate prompt injection by introducing a malicious tool and manipulating intent classification. - Simulate context window limits by restricting the number of tokens processed. - Enhance logging with structured records for each decision and error. - Hierarchical Agent Structures: Manager agents coordinate specialised sub-agents (e.g., designer, coder, tuner), each responsible for a distinct aspect of the workflow . This enables decomposition of complex tasks and parallelisation of subtasks. - Dynamic Tool Selection: Agents maintain a registry of available tools, using semantic indexing, intent classification, and runtime trust scoring to select the most appropriate tool

**Reference code:** [Lab 01](../../labs/01/README.md).

### E02: Implement Trust Decay: Modify the trust scoring so that recent failures decrease a tool’s score

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** Design Exercise: Implement a trust scoring mechanism that decays trust more rapidly after recent failures, and integrates human feedback for disputed tool outcomes. - Add multiplication and division tools. - Implement trust decay for recent failures. - Simulate prompt injection by introducing a malicious tool and manipulating intent classification. - Simulate context window limits by restricting the number of tokens processed. - Enhance logging with structured records for each decision and error.

**Reference code:** [Lab 01](../../labs/01/README.md).

### E03: Simulate Prompt Injection: Add a “malicious” tool to the registry. Write a function that simula

**Reference approach:** Define trusted versus untrusted inputs, a tool allowlist and an explicit unauthorized-call denial case; record a structured audit trace.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** Attack Mechanisms: - Prompt Injection: Malicious prompts are crafted to override intended agent behaviour, often by exploiting weaknesses in intent classification or tool selection logic. - Tool Hijacking: Attackers inject malicious tool definitions into the tool registry, manipulating the agent to select the attacker’s tool for specific tasks. - Add multiplication and division tools. - Implement trust decay for recent failures. - Simulate prompt injection by introducing a malicious tool and manipulating intent classification. - Simulate context window limits by restricting the number of tokens processed. - Enhance logging with structured records for each decision and error.

**Reference code:** [Lab 01](../../labs/01/README.md).

### E04: Context Window Simulation: Simulate a context window limit by restricting the number of tokens 

**Reference approach:** Separate discovery metadata from detailed tool instructions, measure context exposed, and test retrieval and information-isolation edge cases.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Add multiplication and division tools. - Implement trust decay for recent failures. - Simulate prompt injection by introducing a malicious tool and manipulating intent classification. - Simulate context window limits by restricting the number of tokens processed. - Enhance logging with structured records for each decision and error. 1. Define the distinction between AI agents and agentic AI, and explain its significance for real-world applications. 2. Describe the architectures and operational mechanisms underpinning agentic AI systems, with a focus on tool use and workflow control. 3. Analyse the paradoxes and trade-offs that arise as agent capabilities increase, particularly in tool selection, context management, and reliability. 4. Evaluate the limitat

**Reference code:** [Lab 01](../../labs/01/README.md).

### E05: Logging Enhancements: Add structured logging to record every decision, tool invocation, and err

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Structured Logging: Record every decision, tool invocation, and error for auditability. - Attribution: Track which agent or sub-agent made each decision. - Observability: Provide real-time dashboards and alerts for monitoring system health and detecting anomalies. - Human-in-the-Loop Oversight: Enable human review and intervention for high-risk or ambiguous decisions. - Add multiplication and division tools. - Implement trust decay for recent failures. - Simulate prompt injection by introducing a malicious tool and manipulating intent classification. - Simulate context window limits by restricting the number of tokens processed. - Enhance logging with structured records for each decision and error.

**Reference code:** [Lab 01](../../labs/01/README.md).

## Review-question answers

### Q01: What is the difference between an AI agent and agentic AI?

**Answer notes:** 1. Define the distinction between AI agents and agentic AI, and explain its significance for real-world applications. 2. Describe the architectures and operational mechanisms underpinning agentic AI systems, with a focus on tool use and workflow control. 3. Analyse the paradoxes and trade-offs that arise as agent capabilities increase, particularly in tool selection, context management, and reliability. 4. Evaluate the limitat This chapter explores the Agent Capability Paradox—the observation that as AI agents become more capable (e.g., through tool use, adaptive planning, and workflow control), they also introduce new risks, trade-offs, and evaluation challenges that can undermine their practical utility. We ground our discussion in recent literature, focusing on the interplay between agentic architectures, tool orchestration, context management, a

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q02: Why does increasing agent capability sometimes reduce reliability or transparency?

**Answer notes:** As agents become more capable—able to plan, select tools, and adapt dynamically—they also become more complex, harder to interpret, and more susceptible to emergent failures. This is the Agent Capability Paradox: increasing autonomy and flexibility can reduce reliability, transparency, and trust unless new safeguards and evaluation methods are introduced . Artificial intelligence (AI) has rapidly evolved from static, generative models to dynamic, autonomous agents capable of complex reasoning, tool use, and adaptive workflows. As these systems become more sophisticated, a central paradox emerges: increasing agentic capability does not guarantee greater reliability, transparency, or trustworthiness. Instead, new forms of brittleness, emergent failure, and complexity arise, challe

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q03: Describe the lost-in-the-middle effect and its implications for long-context reasoning.

**Answer notes:** 1. Define the distinction between AI agents and agentic AI, and explain its significance for real-world applications. 2. Describe the architectures and operational mechanisms underpinning agentic AI systems, with a focus on tool use and workflow control. 3. Analyse the paradoxes and trade-offs that arise as agent capabilities increase, particularly in tool selection, context management, and reliability. 4. Evaluate the limitat | Capability | Benefit | Trade-Off | |--------------------|-----------------------------------------------------|--------------------------------------------------------------------------------------------------------------------| | Tool Use | Extends agent capabilities beyond LLM knowledge | Increases attack surface, tool selection complexity, and dependency on external systems | | Long Contexts | Enables reasoning over large

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q04: How can runtime trust scoring improve tool selection in agentic AI?

**Answer notes:** - Hierarchical Agent Structures: Manager agents coordinate specialised sub-agents (e.g., designer, coder, tuner), each responsible for a distinct aspect of the workflow . This enables decomposition of complex tasks and parallelisation of subtasks. - Dynamic Tool Selection: Agents maintain a registry of available tools, using semantic indexing, intent classification, and runtime trust scoring to select the most appropriate tool - Tool Selection Complexity: As the number of available tools grows, selecting the right tool becomes a high-dimensional routing and metadata management problem. In multi-server deployments, tool selection must balance semantic intent, tool capability, and system constraints . - Trust and Reliability: Tools may be unavailable, misconfigured, or compromised. Runtime trust scoring frameworks are needed to assess tool reliability

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q05: What are the main security risks associated with agentic tool use?

**Answer notes:** 1. Define the distinction between AI agents and agentic AI, and explain its significance for real-world applications. 2. Describe the architectures and operational mechanisms underpinning agentic AI systems, with a focus on tool use and workflow control. 3. Analyse the paradoxes and trade-offs that arise as agent capabilities increase, particularly in tool selection, context management, and reliability. 4. Evaluate the limitat The Agent Capability Paradox highlights a central tension in the evolution of AI: as agents become more capable, they also become more complex, less transparent, and potentially less reliable. Addressing this paradox requires advances in architecture, evaluation, security, and governance. By understanding the trade-offs and limitations of agentic AI, practitioners can design systems that harness the power of autonomy and tool 

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q06: Explain how hierarchical agent architectures can automate complex workflows. ---

**Answer notes:** - Autonomy: The ability to operate with minimal human intervention. - Reactivity and Proactivity: Responding to changes in the environment and anticipating future needs. - Learning Ability: Continuous self-improvement through experience and feedback. - Hierarchical Architectures: Coordination among specialised sub-agents for complex workflows. - Hierarchical Agent Structures: Manager agents coordinate specialised sub-agents (e.g., designer, coder, tuner), each responsible for a distinct aspect of the workflow . This enables decomposition of complex tasks and parallelisation of subtasks. - Dynamic Tool Selection: Agents maintain a registry of available tools, using semantic indexing, intent classification, and runtime trust scoring to select the most appropriate tool

**Assessment:** definitions, a concrete example, trade-offs and limits.

