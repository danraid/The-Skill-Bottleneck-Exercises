# Chapter 06: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Skill Library Expansion: Add five new skills to your library, each with a description and a bod

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with

**Reference implementation:** [Lab 03](../../labs/03/README.md), [Lab 04](../../labs/04/README.md).

### E02: Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrie

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with

**Reference implementation:** [Lab 03](../../labs/03/README.md), [Lab 04](../../labs/04/README.md).

### E03: Body-aware Retrieval: Modify the retrieval function to use both description and body content. C

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep - Build a minimal skill library with descriptions and bodies. - Implement a retrieval function that selects skills based on query similarity. - Use progressive disclosure to load only descriptions initially, fetching bodies on demand. - Measure context usage and retrieval accuracy. - Explore the impact of distractor skills and body-aware retrieval.

**Reference implementation:** [Lab 03](../../labs/03/README.md), [Lab 04](../../labs/04/README.md).

### E04: Progressive Disclosure Depth: Implement a three-stage disclosure (description → summary → body)

**Suggested approach:** Design controlled evaluation against baseline, ground truth and held-out tasks; report outcome, latency and cost separately.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with

**Reference implementation:** [Lab 03](../../labs/03/README.md), [Lab 04](../../labs/04/README.md).

### E05: Security Simulation: Add a skill with a potentially harmful command in its body. Discuss how pr

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with

**Reference implementation:** [Lab 03](../../labs/03/README.md), [Lab 04](../../labs/04/README.md).

## Review answers

### Q01: What is the main motivation for using progressive disclosure in agentic systems?

**Suggested answer:** - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with 1. Define agent skills, skill retrieval, and progressive disclosure in the context of LLM-based agentic systems. 2. Describe the architectural patterns and trade-offs involved in skill retrieval and progressive disclosure. 3. Explain the challenges and solutions for scaling skill libraries and managing context efficiently. 4. Evaluate the impact of skill organisation and retrieval on agent performance, security, and reliability. 5. Desi

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: How does skill retrieval differ from traditional information retrieval in LLM pipelines?

**Suggested answer:** - Agent Skill: A modular, reusable package of procedural knowledge (instructions, code, resources) that can be loaded by an agent on demand to extend its capabilities , . - Skill Retrieval: The process of selecting a relevant subset of skills from a large library in response to a user query or task , . - Progressive Disclosure: An architectural pattern where only the minimal necessary information about a skill is initially exposed, with 1. Define agent skills, skill retrieval, and progressive disclosure in the context of LLM-based agentic systems. 2. Describe the architectural patterns and trade-offs involved in skill retrieval and progressive disclosure. 3. Explain the challenges and solutions for scaling skill libraries and managing context efficiently. 4. Evaluate the impact of skill organisation and retrieval on agent performance, security, and reliability. 5. Desi

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: What are the trade-offs between retrieval accuracy and context efficiency when hiding skill bod

**Suggested answer:** While hiding skill bodies during initial retrieval saves tokens, it can reduce retrieval accuracy. Studies on large skill libraries (e.g., 80,000+ skills) show that routing based only on descriptions can suffer a 37–44 percentage point drop in accuracy compared to body-aware retrieval . Compressing or distilling descriptions can recover some accuracy, but not all. - Task: Implement a two-stage retrieval pipeline. Measure retrieval accuracy and context usage for both stages. Analyse the trade-off between the number of candidates passed to the second stage and the overall system performance.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: Why is a single level of progressive disclosure usually sufficient?

**Suggested answer:** Controlled studies indicate that a single level of progressive disclosure (description → body) is usually sufficient. Adding further routing layers (e.g., description → summary → body → reference files) rarely helps and can even degrade accuracy . Excessive layering introduces unnecessary complexity and may confuse the agent or dilute actionable information. A primary motivation for progressive disclosure is the finite context window of LLMs. Loading all skills, or even all details of a single skill, can rapidly exhaust available tokens, leading to increased costs, latency, and degraded performance , .

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: How can skill organisation affect agent runtime behaviour and outcomes?

**Suggested answer:** - Controlled Studies: On book-length tasks, progressive disclosure is most beneficial when the agent cannot efficiently navigate raw documents. For large corpora, it outperforms flat loading by degrading more slowly as scale increases . - SkillJuror: Shows that progressive disclosure changes runtime behaviour, increasing the number of actionable resources accessed, with modest but task-dependent gains in outcome quality . 1. Define agent skills, skill retrieval, and progressive disclosure in the context of LLM-based agentic systems. 2. Describe the architectural patterns and trade-offs involved in skill retrieval and progressive disclosure. 3. Explain the challenges and solutions for scaling skill libraries and managing context efficiently. 4. Evaluate the impact of skill organisation and retrieval on agent performance, security, and reliability. 5. Desi

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: What are the main security risks introduced by skill ecosystems, and how can progressive disclo

**Suggested answer:** 1. Skill Library Expansion: Add five new skills to your library, each with a description and a body. Test retrieval accuracy for different queries. 2. Distractor Skills: Introduce distractor skills with misleading descriptions. Observe how retrieval accuracy changes. 3. Body-aware Retrieval: Modify the retrieval function to use both description and body content. Compare retrieval accuracy and context usage. 4. Progressive Disclosure Dep Skill retrieval and progressive disclosure are foundational to the next generation of scalable, efficient, and secure agentic AI systems. By structuring procedural knowledge into modular skills and revealing only what is necessary at each step, these patterns address the practical constraints of context windows, reduce cognitive and computational overhead, and mitigate some security risks. However, the field continues to grapple with re

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: How do benchmarks like SkillRet and SRA-Bench inform the design of retrieval-augmented agent sy

**Suggested answer:** - SKILL.md Specification: The open standard for agent skill packaging . - Model Context Protocol (MCP): Protocol for context management in agentic systems . - Swarm Skills: Portable specification for multi-agent coordination . - SkillRet, SRA-Bench, SkillRouter, SkillJuror, SkillTester: Benchmarks and frameworks for skill retrieval, evaluation, and security. - SkillRet: A large-scale benchmark for skill retrieval, containing over 16,000 public agent skills and thousands of evaluation queries. Fine-tuned retrieval models outperform off-the-shelf baselines, especially in focusing on skill-relevant signals within noisy queries . - SRA-Bench: Evaluates skill retrieval, incorporation, and application across multiple domains and skill-use strategies. Reveals that agents remain sensitive to distra

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
