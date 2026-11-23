# Chapter 18: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Skill Evolution: Extend the platform to support skill versioning and automatic fallback to prev

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Loose Coupling: Skills must be loosely coupled to the agent core, supporting independent evolution and replacement. - Explicit Interfaces: All skills must declare input/output schemas, preconditions, and postconditions. - Versioning: Skills and their interfaces must be versioned to support safe evolution and rollback. - Observability Hooks: All layers must expose hooks for tracing and telemetry. - Security Boundaries: Skills must exec - Extend the agent to support composite skills (skills that invoke other skills). - Implement a trace viewer that aggregates skill invocation logs and highlights failure points. - Add a permission system to restrict which agents can invoke which skills.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E02: Observability: Implement a trace viewer that aggregates skill invocation logs and highlights fa

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Extend the agent to support composite skills (skills that invoke other skills). - Implement a trace viewer that aggregates skill invocation logs and highlights failure points. - Add a permission system to restrict which agents can invoke which skills. 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E03: Security: Add a permission system to restrict which agents can invoke which skills.

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** In multi-agent systems, TRiSM principles are applied to manage explainability, security, and privacy across agent interactions. For instance, access control policies may restrict which agents can invoke sensitive skills, and all skill executions are logged for auditability. - Extend the agent to support composite skills (skills that invoke other skills). - Implement a trace viewer that aggregates skill invocation logs and highlights failure points. - Add a permission system to restrict which agents can invoke which skills.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E04: Composite Skills: Implement a composite skill that chains two or more atomic skills.

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Atomic: Encapsulating a single function (e.g., addition, file upload). - Composite: Orchestrating other skills, supporting hierarchical composition and reuse . - Extend the agent to support composite skills (skills that invoke other skills). - Implement a trace viewer that aggregates skill invocation logs and highlights failure points. - Add a permission system to restrict which agents can invoke which skills.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E05: Benchmarking: Design an experiment to compare the reliability of direct invocation vs. plan-and

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Direct Invocation: The agent calls a skill based on explicit task mapping. Suitable for simple, well-defined tasks. - Reactive Planning (ReAct): The agent alternates between reasoning and acting, selecting skills as needed in response to intermediate results . - Plan-and-Execute: The agent generates a plan (a sequence of skill invocations) and executes it stepwise, monitoring for errors or deviations . - Hierarchical Orchestration: Co 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem

**Source-code reference:** [Lab 14](../../labs/14/README.md).

## Review-question answers

### Q01: What are the key differences between traditional agent architectures and skill-native agentic p

**Model answer:** 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem Traditional agent architectures are typically monolithic, with hard-coded capabilities and limited extensibility. Such agents often lack the flexibility to adapt to new domains or tasks, and their internal logic is tightly coupled to specific workflows. In contrast, skill-native agentic platforms treat skills as modular, composable, and evolvable entities . This architectural shift enables several key advantages:

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: How does skill orchestration improve agent flexibility and reliability?

**Model answer:** 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem The emergence of large language models (LLMs) has catalysed a new generation of agentic AI systems—autonomous, goal-driven agents capable of multi-step reasoning, tool use, and orchestrating workflows across complex environments. A central innovation in these systems is the concept of skills: modular, reusable capabilities that encapsulate domain knowledge, procedural logic, or integrations with external tools and data sources. As the f

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: What are the main observability challenges in skill-native agentic systems, and how can they be

**Model answer:** 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem Skill-native agentic platforms represent a paradigm shift in AI system design, enabling modular, evolvable, and traceable agent capabilities. By adopting explicit skill management, adaptive orchestration, and robust observability, these platforms support reliable and secure deployment of agentic AI in complex, real-world environments. However, challenges in interoperability, security, and governance highlight the need for continued rese

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: Describe the role of security analysis frameworks such as ClawFuzz in skill supply chain manage

**Model answer:** The proliferation of third-party skills introduces a critical attack surface. Malicious or vulnerable skills may inherit the full permissions of the host agent . Multi-layered security analysis frameworks, such as ClawFuzz, combine static analysis, LLM-powered semantic analysis, and adversarial fuzzing to detect and mitigate risks in skill repositories. 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: Explain how operational reliability metrics extend beyond correctness in evaluating agentic sys

**Model answer:** 1. Define the concept of skill-native agentic AI platforms and distinguish them from traditional agent architectures. 2. Describe the architectural components and design patterns underpinning skill-native agent platforms. 3. Explain the role of skills, skill orchestration, and skill evolution in agentic systems. 4. Analyse trade-offs in reliability, observability, and security for production-grade agentic platforms. 5. Design and implem This chapter presents a comprehensive reference architecture for a skill-native agent platform. We synthesise recent advances in agentic AI, distributed systems, and operational reliability, grounding our discussion in empirical findings and architectural proposals from the literature. The goal is to provide a robust blueprint for building agentic systems that are modular, evolvable, observable, and secure—capable of supporting real-wor

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
