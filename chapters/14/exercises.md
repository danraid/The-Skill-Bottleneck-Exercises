# Chapter 14: Enterprise Agent Platforms

## Exercises

### E01

Threat Modelling: Draw a threat model for an MCP-based agent platform, identifying key components, trust boundaries, and potential attack vectors.

### E02

Security Audit: Using the lab specification, register a new tool with subtle prompt injection and test whether the auditing tool detects it.

### E03

Governance Simulation: Implement a simple governance checkpoint in your agent workflow. Measure the impact on latency and user experience.

### E04

Attack Simulation: Attempt to exploit a registered tool by crafting malicious metadata. Observe the agent's behaviour with and without runtime validation.

### E05

Evaluation Pipeline: Design a rubric for automated evaluation of agent responses. Compare the agreement between your rubric-based judge and human raters.

### E06

Multi-Agent Coordination: Design a workflow where two agents must collaborate via MCP to complete a task. Identify potential points of failure and propose mitigation strategies.

### E07

Memory Integration: Extend the agent with a persistent memory module. Simulate a memory poisoning attack and evaluate the effectiveness of isolation and trust scoring mechanisms. ---

## Review questions

### Q01

What are the main architectural components of an enterprise agent platform?

### Q02

How does the Model Context Protocol (MCP) enable tool integration, and what are its main security risks?

### Q03

What is tool poisoning, and why is it particularly challenging to defend against in LLM agent ecosystems?

### Q04

Describe the trade-offs between agent autonomy and governance in enterprise environments.

### Q05

What mechanisms can be used to audit and mitigate security risks in MCP-based agent platforms?

### Q06

How does Zero-Trust Architecture differ from traditional perimeter-based security in the context of agentic AI?

### Q07

Why is automated evaluation of agent outputs both necessary and risky in enterprise deployments?

### Q08

What are the limitations of current MCP security tools and frameworks?

### Q09

How do memory and knowledge modules contribute to agent performance and risk?

### Q10

What are the challenges of multi-agent collaboration in enterprise settings? ---

## Reference laboratories

- [Lab 14](../../labs/14/README.md)
