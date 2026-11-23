# Chapter 12: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Threat Modelling: Draw a diagram of the MCP tool invocation pipeline, marking all trust boundar

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Model Context Protocol (MCP): An open standard for bi-directional communication and dynamic discovery between AI models and external tools/resources . - Tool Boundary: The logical and operational separation between the LLM agent and the external tool or service it invokes. - Tool Poisoning: The embedding of malicious instructions or misleading metadata in tool descriptions or responses to manipulate agent behaviour . - Trust Boundary: Each stage involves distinct trust boundaries and potential attack vectors, which are explored in detail in subsequent sections.

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E02: Static Analysis Extension: Extend the Python lab to include detection of prompt injection patte

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Extend static analysis to detect prompt injection patterns (e.g., “as an AI assistant, you must…”). - Implement a local proxy that intercepts tool calls and responses, applying both static and semantic checks before forwarding to the agent. - Integrate LLM-based semantic analysis for deeper inspection of tool descriptions and responses. - Tool Poisoning: Malicious tool descriptions or responses that manipulate agent reasoning . - Prompt Injection: Injecting adversarial instructions via tool metadata or responses. - Server Hijacking: Registering or taking over MCP servers to serve malicious tools . - Rug Pull Attacks: Withdrawing or altering tool functionality after adoption . - Credential Theft: Exfiltrating secrets via tool responses or side channels . - Supply Chain 

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E03: Runtime Defence Simulation: Implement a proxy that intercepts tool calls and responses, applyin

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Extend static analysis to detect prompt injection patterns (e.g., “as an AI assistant, you must…”). - Implement a local proxy that intercepts tool calls and responses, applying both static and semantic checks before forwarding to the agent. - Integrate LLM-based semantic analysis for deeper inspection of tool descriptions and responses. - MCP-Scanner: Automatically scans MCP servers for vulnerabilities across tools, prompts, and resources, using keyword detection, semantic analysis, and LLM-based evaluation . - McpSafetyScanner: Audits MCP servers for adversarial samples, vulnerabilities, and generates security reports . - SHIELDMCP: Acts as a transparent proxy, performing pre-call description integrity checks, outbound parameter sanitisation, and post-response analysi

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E04: Governance Policy Design: Draft a policy for human approval checkpoints in an MCP-enabled workf

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** In a production enterprise data lakehouse, agents ran as service identities, spawned sub-agents, and chained tool calls across data domains. Existing governance controls failed to detect out-of-scope catalogue reads and unauthorised data exports. Remediation required embedding governance controls directly into the agent architecture, including human approval checkpoints and agent-level action logging . Traditional enterprise governance controls—catalogue policies, audit logs, and permission models—often fail to capture agentic tool use, as agents may spawn sub-agents, chain tool calls, or operate under service identities invisible to existing controls . The Human-Centred Governance Architecture (HCGA) addresses these gaps with:

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E05: Empirical Evaluation: Using open-source MCP servers (e.g., from GitHub), run your scanner and r

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - MCP-Scanner: Automatically scans MCP servers for vulnerabilities across tools, prompts, and resources, using keyword detection, semantic analysis, and LLM-based evaluation . - McpSafetyScanner: Audits MCP servers for adversarial samples, vulnerabilities, and generates security reports . - SHIELDMCP: Acts as a transparent proxy, performing pre-call description integrity checks, outbound parameter sanitisation, and post-response analysi - Model Context Protocol (MCP): An open standard for bi-directional communication and dynamic discovery between AI models and external tools/resources . - Tool Boundary: The logical and operational separation between the LLM agent and the external tool or service it invokes. - Tool Poisoning: The embedding of malicious instructions or misleading metadata in tool descriptions or responses to manipulate agent behaviour . - Trust Boundary:

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E06: Exercise 1: MCP Tool Invocation Pipeline Diagram - Draw a detailed diagram of the MCP tool invo

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Model Context Protocol (MCP): An open standard for bi-directional communication and dynamic discovery between AI models and external tools/resources . - Tool Boundary: The logical and operational separation between the LLM agent and the external tool or service it invokes. - Tool Poisoning: The embedding of malicious instructions or misleading metadata in tool descriptions or responses to manipulate agent behaviour . - Trust Boundary: - MCP Host: The agent or platform that orchestrates tool discovery and invocation. It acts as the primary decision-maker, selecting which tools to use and how to use them. - MCP Server: The external service exposing one or more tools, described via natural-language and structured metadata. Each MCP server may host multiple tools, each with its own interface and operational policies. - Registry: A directory or marketplace where MCP serve

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E07: Exercise 2: Advanced Static Analysis - Extend the provided Python lab to detect additional patt

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Extend static analysis to detect prompt injection patterns (e.g., “as an AI assistant, you must…”). - Implement a local proxy that intercepts tool calls and responses, applying both static and semantic checks before forwarding to the agent. - Integrate LLM-based semantic analysis for deeper inspection of tool descriptions and responses. 1. Creation: Tool development, metadata authoring, and initial registration. This phase is vulnerable to supply chain attacks and tool poisoning. 2. Deployment: Publishing to registries, making tools discoverable. Weak vetting at this stage can allow malicious or compromised tools to enter the ecosystem. 3. Operation: Live invocation by agents, parameter passing, and result delivery. Runtime attacks, such as prompt injection and credent

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E08: Exercise 3: Proxy-Based Runtime Defence - Implement a local proxy that intercepts all MCP tool 

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Extend static analysis to detect prompt injection patterns (e.g., “as an AI assistant, you must…”). - Implement a local proxy that intercepts tool calls and responses, applying both static and semantic checks before forwarding to the agent. - Integrate LLM-based semantic analysis for deeper inspection of tool descriptions and responses. - MCP-Scanner: Automatically scans MCP servers for vulnerabilities across tools, prompts, and resources, using keyword detection, semantic analysis, and LLM-based evaluation . - McpSafetyScanner: Audits MCP servers for adversarial samples, vulnerabilities, and generates security reports . - SHIELDMCP: Acts as a transparent proxy, performing pre-call description integrity checks, outbound parameter sanitisation, and post-response analysi

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E09: Exercise 4: Governance Policy Drafting - Draft a governance policy for MCP-enabled workflows, s

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Task-scoped agent credentials: Agents are granted only the minimum permissions required for a specific task. - Human approval checkpoints: High-risk transitions require explicit human approval. - Agent-level action logging: Every agent action is logged for auditability. - Non-inheritance of credentials: Credentials are not inherited across delegation, preventing privilege escalation. - Operator override and rollback: Human operators c Traditional enterprise governance controls—catalogue policies, audit logs, and permission models—often fail to capture agentic tool use, as agents may spawn sub-agents, chain tool calls, or operate under service identities invisible to existing controls . The Human-Centred Governance Architecture (HCGA) addresses these gaps with:

**Reference implementation:** [Lab 08](../../labs/08/README.md).

### E10: Exercise 5: Empirical Security Evaluation - Collect a set of open-source MCP servers from publi

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - MCP Host: The agent or platform that orchestrates tool discovery and invocation. It acts as the primary decision-maker, selecting which tools to use and how to use them. - MCP Server: The external service exposing one or more tools, described via natural-language and structured metadata. Each MCP server may host multiple tools, each with its own interface and operational policies. - Registry: A directory or marketplace where MCP serve - MCP-Scanner: Automatically scans MCP servers for vulnerabilities across tools, prompts, and resources, using keyword detection, semantic analysis, and LLM-based evaluation . - McpSafetyScanner: Audits MCP servers for adversarial samples, vulnerabilities, and generates security reports . - SHIELDMCP: Acts as a transparent proxy, performing pre-call description integrity checks, outbound parameter sanitisation, and post-response analysi

**Reference implementation:** [Lab 08](../../labs/08/README.md).

## Review answers

### Q01: What is the Model Context Protocol (MCP), and why has it become central to agentic AI systems?

**Suggested answer:** The transformation of Large Language Model (LLM) agents from passive assistants into autonomous, tool-using, and collaborative systems has fundamentally altered the landscape of AI application design. Central to this evolution is the Model Context Protocol (MCP), an open standard that enables LLMs to discover, describe, and invoke external tools and resources in a unified, interoperable manner . MCP has rapidly become the de facto indus The Model Context Protocol has unlocked a new era of interoperable, tool-augmented agentic AI, but at the cost of expanded attack surfaces and complex governance challenges. Secure, reliable, and auditable tool integration requires a multi-layered approach, combining static and dynamic analysis, runtime validation, robust governance, and continuous evaluation. As the ecosystem matures, balancing capability, interoperability, and securit

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: Explain the concept of a trust boundary in the context of MCP. Give two examples.

**Suggested answer:** 1. Define the Model Context Protocol (MCP) and explain its role in LLM-based agentic AI systems. 2. Describe the architectural components and trust boundaries of MCP-enabled tool integration. 3. Identify common security threats and vulnerabilities in the MCP ecosystem, including tool poisoning and supply chain risks. 4. Evaluate governance and mitigation strategies for secure, auditable, and policy-compliant tool use. 5. Implement basic - Model Context Protocol (MCP): An open standard for bi-directional communication and dynamic discovery between AI models and external tools/resources . - Tool Boundary: The logical and operational separation between the LLM agent and the external tool or service it invokes. - Tool Poisoning: The embedding of malicious instructions or misleading metadata in tool descriptions or responses to manipulate agent behaviour . - Trust Boundary:

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: What are tool poisoning attacks, and why are they particularly challenging to defend against in

**Suggested answer:** 1. Creation: Tool development, metadata authoring, and initial registration. This phase is vulnerable to supply chain attacks and tool poisoning. 2. Deployment: Publishing to registries, making tools discoverable. Weak vetting at this stage can allow malicious or compromised tools to enter the ecosystem. 3. Operation: Live invocation by agents, parameter passing, and result delivery. Runtime attacks, such as prompt injection and credent - Tool Poisoning: Malicious tool descriptions or responses that manipulate agent reasoning . - Prompt Injection: Injecting adversarial instructions via tool metadata or responses. - Server Hijacking: Registering or taking over MCP servers to serve malicious tools . - Rug Pull Attacks: Withdrawing or altering tool functionality after adoption . - Credential Theft: Exfiltrating secrets via tool responses or side channels . - Supply Chain 

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: Describe two open-source tools or frameworks for MCP security scanning or runtime defence.

**Suggested answer:** 1. Define the Model Context Protocol (MCP) and explain its role in LLM-based agentic AI systems. 2. Describe the architectural components and trust boundaries of MCP-enabled tool integration. 3. Identify common security threats and vulnerabilities in the MCP ecosystem, including tool poisoning and supply chain risks. 4. Evaluate governance and mitigation strategies for secure, auditable, and policy-compliant tool use. 5. Implement basic Several open-source tools and frameworks have been developed to detect and mitigate MCP vulnerabilities:

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: What governance mechanisms are necessary to ensure safe and auditable tool use in enterprise ag

**Suggested answer:** - Model Context Protocol (MCP): An open standard for bi-directional communication and dynamic discovery between AI models and external tools/resources . - Tool Boundary: The logical and operational separation between the LLM agent and the external tool or service it invokes. - Tool Poisoning: The embedding of malicious instructions or misleading metadata in tool descriptions or responses to manipulate agent behaviour . - Trust Boundary: 1. Define the Model Context Protocol (MCP) and explain its role in LLM-based agentic AI systems. 2. Describe the architectural components and trust boundaries of MCP-enabled tool integration. 3. Identify common security threats and vulnerabilities in the MCP ecosystem, including tool poisoning and supply chain risks. 4. Evaluate governance and mitigation strategies for secure, auditable, and policy-compliant tool use. 5. Implement basic

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: Discuss the trade-offs between interoperability and security in MCP-enabled tool integration.

**Suggested answer:** 1. Define the Model Context Protocol (MCP) and explain its role in LLM-based agentic AI systems. 2. Describe the architectural components and trust boundaries of MCP-enabled tool integration. 3. Identify common security threats and vulnerabilities in the MCP ecosystem, including tool poisoning and supply chain risks. 4. Evaluate governance and mitigation strategies for secure, auditable, and policy-compliant tool use. 5. Implement basic This chapter provides a comprehensive exploration of MCP-enabled agentic AI, focusing on architecture, terminology, security landscape, and governance strategies. We aim to equip practitioners and researchers with both conceptual foundations and practical guidance for secure, reliable, and auditable tool integration.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: How do supply chain attacks manifest in the MCP ecosystem, and what mitigation strategies are r

**Suggested answer:** 1. Define the Model Context Protocol (MCP) and explain its role in LLM-based agentic AI systems. 2. Describe the architectural components and trust boundaries of MCP-enabled tool integration. 3. Identify common security threats and vulnerabilities in the MCP ecosystem, including tool poisoning and supply chain risks. 4. Evaluate governance and mitigation strategies for secure, auditable, and policy-compliant tool use. 5. Implement basic 1. Creation: Tool development, metadata authoring, and initial registration. This phase is vulnerable to supply chain attacks and tool poisoning. 2. Deployment: Publishing to registries, making tools discoverable. Weak vetting at this stage can allow malicious or compromised tools to enter the ecosystem. 3. Operation: Live invocation by agents, parameter passing, and result delivery. Runtime attacks, such as prompt injection and credent

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
