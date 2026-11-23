# Chapter 05: Worked Answers

The reference responses are based on the corresponding chapter. Open-ended assignments can admit multiple correct designs.

## Exercise solutions

### E01: Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and met

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** 1. Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category. 2. Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval. 3. Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) - Agent Skill: A modular, callable package containing procedural knowledge, instructions, code, and resources, loaded on demand by an agent . - Skill Registry: A structured repository or index of skills, supporting discovery, retrieval, and management at scale . - Progressive Disclosure: A context-management strategy where only minimal skill metadata is initially exposed, with further details loaded as needed . - Skill Retriev

**Reference code:** [Lab 02](../../labs/02/README.md).

### E02: Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant s

**Reference approach:** Construct a baseline and ground-truth tasks, separate development and protected confirmation splits, and report quality, latency, cost and uncertainties independently.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** 1. Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category. 2. Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval. 3. Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) - Metadata-only retrieval: Matching queries to skill names and descriptions. - Body-aware retrieval: Incorporating the full skill body into the retrieval process, improving accuracy but increasing computational cost . - Hybrid retrieval: Combining metadata and body signals, possibly with reranking or semantic augmentation.

**Reference code:** [Lab 02](../../labs/02/README.md).

### E03: Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of quer

**Reference approach:** Separate discovery metadata from detailed tool instructions, measure context exposed, and test retrieval and information-isolation edge cases.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** 1. Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category. 2. Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval. 3. Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) - Context Window Limitations: Only a limited number of tokens can be loaded into the agent’s context at once. Progressive disclosure and compression are essential for scalability. - Latency and Throughput: Retrieval and loading must be fast enough to support interactive agent workflows. - Security and Isolation: Skills must be validated and sandboxed to prevent privilege escalation or supply-chain attacks. - Versioning and Pro

**Reference code:** [Lab 02](../../labs/02/README.md).

### E04: Security Simulation: Add a "trusted" flag to skill metadata. Simulate a scenario where a skill 

**Reference approach:** Define trusted versus untrusted inputs, a tool allowlist and an explicit unauthorized-call denial case; record a structured audit trace.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** 1. Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category. 2. Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval. 3. Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) - Add semantic tags and hierarchical categories. - Implement body-aware retrieval by indexing both description and body. - Simulate progressive disclosure by measuring token usage before and after body loading. - Add a trust/provenance field to metadata and filter retrieval results accordingly.

**Reference code:** [Lab 02](../../labs/02/README.md).

### E05: Skill Evolution: Implement a simple feedback loop where users can rate skill effectiveness, and

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** 1. Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category. 2. Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval. 3. Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) - Agent Skill: A modular, callable package containing procedural knowledge, instructions, code, and resources, loaded on demand by an agent . - Skill Registry: A structured repository or index of skills, supporting discovery, retrieval, and management at scale . - Progressive Disclosure: A context-management strategy where only minimal skill metadata is initially exposed, with further details loaded as needed . - Skill Retriev

**Reference code:** [Lab 02](../../labs/02/README.md).

## Review-question answers

### Q01: Define the difference between a skill, a tool, and a sub-agent in agentic AI systems.

**Answer notes:** - Define the concept of agent skills and distinguish them from tools, sub-agents, and agents. - Explain the architectural foundations and design patterns of large-scale skill registries for LLM-based agents. - Analyse the trade-offs in skill retrieval, organisation, and progressive disclosure for scalable agentic systems. - Evaluate security, trust, and lifecycle governance challenges in skill ecosystems. - Design and implemen The rapid evolution of large language model (LLM) agents from monolithic, all-in-one systems to modular, extensible architectures has brought the concept of skills—reusable, procedural knowledge packages—to the forefront of agentic AI . Skills enable agents to dynamically acquire new capabilities without retraining, supporting flexible, context-efficient, and scalable workflows. This modularity is essential as agentic systems 

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q02: Explain why progressive disclosure is critical for large-scale skill registries.

**Answer notes:** - Define the concept of agent skills and distinguish them from tools, sub-agents, and agents. - Explain the architectural foundations and design patterns of large-scale skill registries for LLM-based agents. - Analyse the trade-offs in skill retrieval, organisation, and progressive disclosure for scalable agentic systems. - Evaluate security, trust, and lifecycle governance challenges in skill ecosystems. - Design and implemen Progressive disclosure is a context-efficiency mechanism: only the minimal necessary metadata (e.g., skill names and short descriptions) is loaded initially, with the full skill body loaded only if selected . This approach is critical for scaling to large registries, as it:

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q03: Discuss the trade-offs between metadata-only and body-aware skill retrieval.

**Answer notes:** - Metadata-only retrieval: Matching queries to skill names and descriptions. - Body-aware retrieval: Incorporating the full skill body into the retrieval process, improving accuracy but increasing computational cost . - Hybrid retrieval: Combining metadata and body signals, possibly with reranking or semantic augmentation. - Metadata-only retrieval (using names and descriptions) is efficient but can lead to significant drops in retrieval accuracy, especially in large, overlapping skill libraries . - Body-aware retrieval (incorporating the full skill body) recovers much of the lost accuracy, as critical signals often reside in the body rather than the metadata. However, it incurs higher computational and context costs. - Hybrid approaches (e.g., 

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q04: Describe two security risks associated with open skill marketplaces and suggest mitigation stra

**Answer notes:** - Define the concept of agent skills and distinguish them from tools, sub-agents, and agents. - Explain the architectural foundations and design patterns of large-scale skill registries for LLM-based agents. - Analyse the trade-offs in skill retrieval, organisation, and progressive disclosure for scalable agentic systems. - Evaluate security, trust, and lifecycle governance challenges in skill ecosystems. - Design and implemen - Open skill marketplaces are vulnerable to supply-chain attacks, including malicious payloads embedded in skill documentation or code . - Document-Driven Implicit Payload Execution (DDIPE) demonstrates that malicious logic can be embedded in code examples or configuration templates, bypassing explicit prompt defences.

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q05: Summarise how skill evolution frameworks (e.g., EvoSkill, SkillGrad) contribute to the maintena

**Answer notes:** - Automated skill discovery and optimisation frameworks (e.g., EvoSkill, SkillGrad) can refine and expand skill libraries based on agent experience and failure analysis . - Evolutionary approaches analyse execution failures, propose new skills or edits, and retain only those that improve validation performance. - Gradient-descent-inspired frameworks treat the skill package as a structured parameter to optimise, using trajector Large-scale skill registries are a cornerstone of scalable, flexible, and trustworthy agentic AI. Their design requires careful attention to context efficiency, retrieval accuracy, security, and lifecycle management. Progressive disclosure, robust routing, and automated skill evolution are key enablers, but significant challenges remain in quality assurance, security, and cross-platform interoperability. As the field matures, 

**Assessment:** definitions, a concrete example, trade-offs and limits.

