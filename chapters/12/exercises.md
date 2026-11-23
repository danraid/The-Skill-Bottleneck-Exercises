# Chapter 12: Model Context Protocol and Tool Boundaries

## Exercises

### E01

Threat Modelling: Draw a diagram of the MCP tool invocation pipeline, marking all trust boundaries. For each boundary, list at least two possible attack vectors.

### E02

Static Analysis Extension: Extend the Python lab to include detection of prompt injection patterns (e.g., “as an AI assistant, you must…”) in tool descriptions.

### E03

Runtime Defence Simulation: Implement a proxy that intercepts tool calls and responses, applying both static and semantic checks before forwarding to the agent.

### E04

Governance Policy Design: Draft a policy for human approval checkpoints in an MCP-enabled workflow. Specify which tool calls require approval and how audit logs should be structured.

### E05

Empirical Evaluation: Using open-source MCP servers (e.g., from GitHub), run your scanner and report the proportion of tools flagged for suspicious metadata. ---

### E06

Exercise 1: MCP Tool Invocation Pipeline Diagram - Draw a detailed diagram of the MCP tool invocation pipeline, including all trust boundaries. - Annotate each boundary with at least two possible attack vectors (e.g., prompt injection, server hijacking).

### E07

Exercise 2: Advanced Static Analysis - Extend the provided Python lab to detect additional patterns, such as: - Prompt injection in tool descriptions (“as an AI assistant, you must…”). - Obfuscated commands (e.g., base64-encoded payloads).

### E08

Exercise 3: Proxy-Based Runtime Defence - Implement a local proxy that intercepts all MCP tool calls and responses. - Apply both static and semantic checks before forwarding data to the agent. - Log all intercepted events for audit and analysis.

### E09

Exercise 4: Governance Policy Drafting - Draft a governance policy for MCP-enabled workflows, specifying: - Which tool calls require human approval. - How audit logs should be structured and reviewed. - Procedures for operator override and rollback.

### E10

Exercise 5: Empirical Security Evaluation - Collect a set of open-source MCP servers from public repositories. - Run your scanner against each server and report: - The proportion of tools flagged for suspicious metadata. - Types of vulnerabilities detected. ---

## Review questions

### Q01

What is the Model Context Protocol (MCP), and why has it become central to agentic AI systems?

### Q02

Explain the concept of a trust boundary in the context of MCP. Give two examples.

### Q03

What are tool poisoning attacks, and why are they particularly challenging to defend against in LLM agent systems?

### Q04

Describe two open-source tools or frameworks for MCP security scanning or runtime defence.

### Q05

What governance mechanisms are necessary to ensure safe and auditable tool use in enterprise agentic AI deployments?

### Q06

Discuss the trade-offs between interoperability and security in MCP-enabled tool integration.

### Q07

How do supply chain attacks manifest in the MCP ecosystem, and what mitigation strategies are recommended? ---

## Laboratories

- [Lab 08](../../labs/08/README.md)
