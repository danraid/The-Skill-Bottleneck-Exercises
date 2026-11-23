# Chapter 07: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Conceptual: Explain why progressive disclosure is more effective than loading all skill bodies 

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Define the concepts of context budgeting and skill interference in LLM-based agentic systems. 2. Explain the architectural mechanisms—such as progressive disclosure and skill retrieval—that address context limitations. 3. Analyse the trade-offs between context window usage, skill modularity, and agent performance. 4. Identify common pitfalls and security risks associated with large skill libraries and context management. 5. Design an - Context Window: The maximum number of tokens (words, instructions, data) an LLM can process at once. - Skill: A modular, reusable package of procedural knowledge, instructions, or code that can be loaded by an agent on demand . - Progressive Disclosure: A context management strategy where only high-level skill descriptions are initially exposed, with detailed content loaded as needed . - Skill Retrieval Augmentation (SRA): The process

**Reference implementation:** [Lab 04](../../labs/04/README.md), [Lab 05](../../labs/05/README.md).

### E02: Practical: Modify the lab to use a two-stage retrieval pipeline (initial retrieval by descripti

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Extension Exercises: - Implement a two-stage retrieval pipeline (initial retrieval by description, reranking by partial body content). - Add a static check to prevent loading of a simulated “malicious” skill. - Implement skill compression to remove non-actionable content before loading. Two-Stage Pipeline: 1. Initial Retrieval: Use a fast, embedding-based retriever to select a candidate set of skills based on descriptions. 2. Reranking: Apply a more sophisticated reranker (possibly LLM-based or body-aware) to reorder the candidates, considering both descriptions and partial body content.

**Reference implementation:** [Lab 04](../../labs/04/README.md), [Lab 05](../../labs/05/README.md).

### E03: Analysis: Using the lab, measure how agent accuracy changes as you increase the number of distr

**Suggested approach:** Design controlled evaluation against baseline, ground truth and held-out tasks; report outcome, latency and cost separately.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Vary the number of distractor skills (irrelevant but loaded into context). - Measure agent performance on a set of tasks (e.g., accuracy, latency). Evaluation Metrics: - Routing Accuracy: Proportion of tasks where the correct skill is selected. - Token Efficiency: Ratio of task success to tokens consumed. - Interference Sensitivity: Change in performance as the number of distractor skills increases.

**Reference implementation:** [Lab 04](../../labs/04/README.md), [Lab 05](../../labs/05/README.md).

### E04: Security: Add a “malicious” skill to the library. Design a simple static check to prevent its l

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Simulate a “malicious” skill that, if loaded, triggers an alert (do not execute real code). - Implement a static check to prevent its loading. Extension Exercises: - Implement a two-stage retrieval pipeline (initial retrieval by description, reranking by partial body content). - Add a static check to prevent loading of a simulated “malicious” skill. - Implement skill compression to remove non-actionable content before loading.

**Reference implementation:** [Lab 04](../../labs/04/README.md), [Lab 05](../../labs/05/README.md).

### E05: Extension: Implement a basic skill compression step that removes non-actionable content from sk

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Extension Exercises: - Implement a two-stage retrieval pipeline (initial retrieval by description, reranking by partial body content). - Add a static check to prevent loading of a simulated “malicious” skill. - Implement skill compression to remove non-actionable content before loading. Algorithmic Exercise: Implement a skill compression pipeline that: - Removes non-actionable content from skill bodies. - Generates concise, body-distilled descriptions for routing. - Validates that compressed skills retain functional quality.

**Reference implementation:** [Lab 04](../../labs/04/README.md), [Lab 05](../../labs/05/README.md).

## Review answers

### Q01: What is the main motivation for context budgeting in LLM-based agent systems?

**Suggested answer:** 1. Define the concepts of context budgeting and skill interference in LLM-based agentic systems. 2. Explain the architectural mechanisms—such as progressive disclosure and skill retrieval—that address context limitations. 3. Analyse the trade-offs between context window usage, skill modularity, and agent performance. 4. Identify common pitfalls and security risks associated with large skill libraries and context management. 5. Design an Context budgeting and skill interference are central challenges in the design and deployment of scalable, reliable, and secure LLM-based agentic systems. Progressive disclosure, efficient skill retrieval, and careful skill organisation offer practical solutions, but introduce new trade-offs and risks. As skill libraries and agent ecosystems continue to grow, ongoing research is needed to develop robust retrieval, compression, and securi

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: How does skill interference manifest, and what are its practical consequences?

**Suggested answer:** The evolution of Large Language Model (LLM) agents from monolithic, prompt-driven systems to modular, skill-augmented architectures has introduced new complexities in system design and operation. Two interrelated challenges—context budgeting and skill interference—have become central to the practical deployment of these systems. Context budgeting and skill interference are central challenges in the design and deployment of scalable, reliable, and secure LLM-based agentic systems. Progressive disclosure, efficient skill retrieval, and careful skill organisation offer practical solutions, but introduce new trade-offs and risks. As skill libraries and agent ecosystems continue to grow, ongoing research is needed to develop robust retrieval, compression, and securi

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: Describe the progressive disclosure pattern and its empirical benefits.

**Suggested answer:** Empirical Findings: Progressive disclosure can reduce upfront token overhead by over 90%, decrease session token consumption, and lower operational costs, all while maintaining or improving tool-selection accuracy . However, the benefit is task-dependent and may be redundant if the agent or framework already implements strong retrieval and navigation capabilities . Empirical evidence suggests that a single level of progressive disclosure is usually sufficient; deeper hierarchies may degrade accuracy or introduce unnecessary complexity .

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: Why does hiding skill bodies during routing reduce retrieval accuracy, and how can this be miti

**Suggested answer:** - Small Libraries: Skills can be loaded explicitly by name, with minimal routing overhead. - Large Libraries: Require sophisticated retrieval and routing mechanisms. Hiding skill bodies (for token efficiency) can reduce routing accuracy by up to 44 percentage points, but body-distilled descriptions and compact rerankers can recover much of this gap . Benchmark Insights: Off-the-shelf retrievers struggle on large skill libraries. Fine-tuned, body-aware retrievers (which consider both descriptions and implementation details) achieve significantly higher routing accuracy . Hiding skill bodies for token efficiency can reduce routing accuracy by up to 44 percentage points, but body-distilled descriptions and compact rerankers can recover much of this gap.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: What are the main security risks associated with third-party skill loading?

**Suggested answer:** 1. Define the concepts of context budgeting and skill interference in LLM-based agentic systems. 2. Explain the architectural mechanisms—such as progressive disclosure and skill retrieval—that address context limitations. 3. Analyse the trade-offs between context window usage, skill modularity, and agent performance. 4. Identify common pitfalls and security risks associated with large skill libraries and context management. 5. Design an - Context Window: The maximum number of tokens (words, instructions, data) an LLM can process at once. - Skill: A modular, reusable package of procedural knowledge, instructions, or code that can be loaded by an agent on demand . - Progressive Disclosure: A context management strategy where only high-level skill descriptions are initially exposed, with detailed content loaded as needed . - Skill Retrieval Augmentation (SRA): The process

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: How do benchmarks such as SkillRet and SRA-Bench inform our understanding of skill retrieval ch

**Suggested answer:** Recent benchmarks such as SkillRet and SRA-Bench provide large-scale datasets for evaluating skill retrieval and routing in LLM agents . Key findings include: 1. Define the concepts of context budgeting and skill interference in LLM-based agentic systems. 2. Explain the architectural mechanisms—such as progressive disclosure and skill retrieval—that address context limitations. 3. Analyse the trade-offs between context window usage, skill modularity, and agent performance. 4. Identify common pitfalls and security risks associated with large skill libraries and context management. 5. Design an

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
