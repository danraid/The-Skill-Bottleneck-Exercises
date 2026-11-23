# Chapter 14: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Threat Modelling: Draw a threat model for an MCP-based agent platform, identifying key componen

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities, - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E02: Security Audit: Using the lab specification, register a new tool with subtle prompt injection a

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 2. Tool Registration - Register a benign tool (e.g., calculator or file reader) with the MCP server, providing clear and safe metadata. - Register a tool with intentionally poisoned metadata (e.g., embedded prompt injection or exfiltration instruction). - Modify the poisoned tool to use more subtle prompt injection techniques and observe detection rates. - Integrate a runtime validation proxy and compare agent behaviour with and without the proxy in place. - Implement a governance checkpoint that requires multi-factor approval for sensitive actions.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E03: Governance Simulation: Implement a simple governance checkpoint in your agent workflow. Measure

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 6. Governance Controls - Implement a simple approval checkpoint (e.g., requiring human confirmation before executing high-risk tool calls). - Measure the impact on workflow latency and user experience. 3. Agent Integration - Configure the agent to discover and invoke tools via the MCP protocol. - Implement a basic workflow where the agent selects and calls tools based on user input.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E04: Attack Simulation: Attempt to exploit a registered tool by crafting malicious metadata. Observe

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Modify the poisoned tool to use more subtle prompt injection techniques and observe detection rates. - Integrate a runtime validation proxy and compare agent behaviour with and without the proxy in place. - Implement a governance checkpoint that requires multi-factor approval for sensitive actions. Tool poisoning, where malicious instructions are embedded in tool metadata or responses, is the most prevalent and impactful client-side vulnerability in MCP-based systems ; . Prompt injection attacks can further manipulate agent behaviour, often bypassing traditional input validation.

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E05: Evaluation Pipeline: Design a rubric for automated evaluation of agent responses. Compare the a

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Rubric-Based Assessment: Defines explicit criteria for correctness, safety, and compliance. - Judge Reliability: Measures agreement between automated and human raters. - Pipeline Architecture: Embeds evaluation within the agent inference loop for continuous monitoring. - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E06: Multi-Agent Coordination: Design a workflow where two agents must collaborate via MCP to comple

**Suggested implementation:** Specify bounded task execution, explicit delegation rules, least-privilege profiles and failure-recovery checkpoints.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** In a multi-agent scenario, several LLM agents may coordinate via MCP to complete a complex workflow. For instance, one agent may handle data extraction, another may perform analysis, and a third may generate reports. Coordination is achieved through shared memory modules and event-driven messaging, with MCP serving as the common interface for tool invocation. 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities,

**Source-code reference:** [Lab 14](../../labs/14/README.md).

### E07: Memory Integration: Extend the agent with a persistent memory module. Simulate a memory poisoni

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th 1. LLM Core: The reasoning engine, responsible for planning, decision-making, and natural language understanding. This component interprets user intent, decomposes tasks, and orchestrates tool use. 2. Tool Interface Layer: Standardised connectors (often via MCP) that allow the agent to discover and invoke external tools and services. This layer abstracts the details of tool invocation and response handling. 3. Memory and Knowledge Modul

**Source-code reference:** [Lab 14](../../labs/14/README.md).

## Review-question answers

### Q01: What are the main architectural components of an enterprise agent platform?

**Model answer:** 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities, The Cineca Agentic Platform (CAP) exemplifies a full-stack, cloud-native system for deploying multi-tenant LLM agents in enterprise environments . CAP integrates:

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: How does the Model Context Protocol (MCP) enable tool integration, and what are its main securi

**Model answer:** 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities, 1. LLM Core: The reasoning engine, responsible for planning, decision-making, and natural language understanding. This component interprets user intent, decomposes tasks, and orchestrates tool use. 2. Tool Interface Layer: Standardised connectors (often via MCP) that allow the agent to discover and invoke external tools and services. This layer abstracts the details of tool invocation and response handling. 3. Memory and Knowledge Modul

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: What is tool poisoning, and why is it particularly challenging to defend against in LLM agent e

**Model answer:** - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: Describe the trade-offs between agent autonomy and governance in enterprise environments.

**Model answer:** 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities, - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: What mechanisms can be used to audit and mitigate security risks in MCP-based agent platforms?

**Model answer:** - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: How does Zero-Trust Architecture differ from traditional perimeter-based security in the contex

**Model answer:** 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities, This chapter provides a structured and in-depth overview of enterprise agent platforms, focusing on their architecture, security, governance, and practical deployment considerations. It addresses the interplay between technical design, operational constraints, and the unique risks and opportunities presented by agentic AI in enterprise settings.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q07: Why is automated evaluation of agent outputs both necessary and risky in enterprise deployments

**Model answer:** Automated evaluation pipelines, often using LLMs as judges, are now essential for scalable quality and safety assessment. However, the evaluator itself must be scrutinised for bias, reliability, and alignment with enterprise policies . - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q08: What are the limitations of current MCP security tools and frameworks?

**Model answer:** - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q09: How do memory and knowledge modules contribute to agent performance and risk?

**Model answer:** - Security Gaps: Many vulnerabilities, especially tool poisoning and prompt injection, remain difficult to detect and mitigate, particularly as attackers develop more sophisticated payloads ; . - Governance Complexity: Embedding effective governance controls without unduly hindering agent autonomy or operational efficiency is an ongoing challenge . - Evaluation Reliability: Automated judges can introduce bias or propagate errors, and th 1. LLM Core: The reasoning engine, responsible for planning, decision-making, and natural language understanding. This component interprets user intent, decomposes tasks, and orchestrates tool use. 2. Tool Interface Layer: Standardised connectors (often via MCP) that allow the agent to discover and invoke external tools and services. This layer abstracts the details of tool invocation and response handling. 3. Memory and Knowledge Modul

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q10: What are the challenges of multi-agent collaboration in enterprise settings? ---

**Model answer:** Enterprise agent platforms represent a transformative convergence of advanced language models, autonomous tool use, and collaborative multi-agent systems, all operationalised within the stringent requirements of enterprise IT. These platforms are evolving rapidly, shifting from passive assistants to autonomous, tool-using, and collaborative systems capable of executing complex, long-horizon tasks across web, software, and physical envir 1. Define the core concepts and terminology of enterprise agent platforms, especially those built on Large Language Models (LLMs) and the Model Context Protocol (MCP). 2. Describe the reference architectures and modular components of enterprise agentic systems. 3. Analyse the security, governance, and operational trade-offs inherent in deploying agentic AI in enterprise environments. 4. Evaluate the main attack vectors, vulnerabilities,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
