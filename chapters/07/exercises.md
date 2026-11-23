# Chapter 07: Context Budgeting and Skill Interference

## Exercises

### E01

Conceptual: Explain why progressive disclosure is more effective than loading all skill bodies into the context window for large skill libraries.

### E02

Practical: Modify the lab to use a two-stage retrieval pipeline (initial retrieval by description, reranking by partial body content).

### E03

Analysis: Using the lab, measure how agent accuracy changes as you increase the number of distractor skills. Plot and interpret the results.

### E04

Security: Add a “malicious” skill to the library. Design a simple static check to prevent its loading.

### E05

Extension: Implement a basic skill compression step that removes non-actionable content from skill bodies before loading. ---

## Review questions

### Q01

What is the main motivation for context budgeting in LLM-based agent systems?

### Q02

How does skill interference manifest, and what are its practical consequences?

### Q03

Describe the progressive disclosure pattern and its empirical benefits.

### Q04

Why does hiding skill bodies during routing reduce retrieval accuracy, and how can this be mitigated?

### Q05

What are the main security risks associated with third-party skill loading?

### Q06

How do benchmarks such as SkillRet and SRA-Bench inform our understanding of skill retrieval challenges? ---

## Laboratories

- [Lab 04](../../labs/04/README.md)
- [Lab 05](../../labs/05/README.md)
