# Chapter 05: Designing Large-Scale Skill Registries

## Practical exercises

### E01

Skill Registry Expansion: Extend the sample registry to 20+ skills with diverse domains and metadata. Implement a function to list all skills in a given category.

### E02

Retrieval Evaluation: Measure retrieval accuracy by creating test queries with known relevant skills. Compare metadata-only vs. body-aware retrieval.

### E03

Progressive Disclosure Simulation: Track and plot the number of tokens loaded for a set of queries under (a) full upfront loading and (b) progressive disclosure.

### E04

Security Simulation: Add a "trusted" flag to skill metadata. Simulate a scenario where a skill with a suspicious body is flagged and excluded from retrieval results.

### E05

Skill Evolution: Implement a simple feedback loop where users can rate skill effectiveness, and the registry updates a "quality" score in metadata. ---

## Review questions

### Q01

Define the difference between a skill, a tool, and a sub-agent in agentic AI systems.

### Q02

Explain why progressive disclosure is critical for large-scale skill registries.

### Q03

Discuss the trade-offs between metadata-only and body-aware skill retrieval.

### Q04

Describe two security risks associated with open skill marketplaces and suggest mitigation strategies.

### Q05

Summarise how skill evolution frameworks (e.g., EvoSkill, SkillGrad) contribute to the maintenance of skill registries. ---

## Reference laboratories

- [Lab 02](../../labs/02/README.md)
