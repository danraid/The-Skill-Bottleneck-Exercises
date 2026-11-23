# Chapter 09: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Profile Extension: Modify the schema to support runtime drift tracking (e.g., add a runtimecont

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Design Exercise: Extend this algorithm to support dynamic runtime checks, such as environment drift or dependency mismatches. For example, compare the declared runtimecontext against the current execution environment and flag discrepancies. Design Exercise: Extend the CapAgent schema to support a runtimecontext field, capturing OS, Python version, and dependency versions. Discuss how this field supports reproducibility and drift detection.

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E02: Adversarial Profile Detection: Implement a pool-side validator that checks for suspicious capab

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Agent Profile: A structured, machine-readable representation of an agent’s capabilities, constraints, identity, and provenance, designed for reuse across tasks and orchestration contexts. - Orchestration: The process of coordinating multiple agents, including task allocation, message routing, and execution monitoring. - Coordination: The mechanisms by which agents interact and collaborate to achieve shared or interdependent goals, oft def validateprofile(profile: AgentProfile, signature: bytes, publickeypem: bytes): publickey = serialization.loadpempublickey(publickeypem) try: publickey.verify( signature, profile.json().encode(), padding.PSS(mgf=padding.MGF1(hashes.SHA256()), saltlength=padding.PSS.MAXLENGTH), hashes.SHA256() ) Additional checks for conflicting or excessive capabilities e.g., check for duplicate capability names or overbroad constraints return True e

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E03: Delegation Chain Audit: Write a function that reconstructs and visualises the delegation chain 

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Suppose an orchestrator issues a profile to Agent A, which then delegates a subset of its capabilities to Agent B. Each delegation step appends to the chainofdelegation, and the resulting profile for Agent B includes a restricted set of capabilities, updated provenance, and a cryptographic signature from Agent A. This enables traceable, least-privilege delegation and supports post-hoc audit. - Agent Profile: A structured, machine-readable representation of an agent’s capabilities, constraints, identity, and provenance, designed for reuse across tasks and orchestration contexts. - Orchestration: The process of coordinating multiple agents, including task allocation, message routing, and execution monitoring. - Coordination: The mechanisms by which agents interact and collaborate to achieve shared or interdependent goals, oft

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E04: Failure Attribution: Simulate a multi-agent workflow and use structured logs to attribute a syn

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Structured Telemetry: Frameworks such as AgentTelemetry and AgenTracer demonstrate the need for profile-linked span taxonomy and failure tracing . Without structured observability, failures are difficult to attribute, impeding system reliability. - Agent Profile: A structured, machine-readable representation of an agent’s capabilities, constraints, identity, and provenance, designed for reuse across tasks and orchestration contexts. - Orchestration: The process of coordinating multiple agents, including task allocation, message routing, and execution monitoring. - Coordination: The mechanisms by which agents interact and collaborate to achieve shared or interdependent goals, oft

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E05: Privacy Audit: Instrument inter-agent messages and demonstrate detection of sensitive data leak

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Adversarial Manipulation: Malicious actors may craft deceptive profiles to hijack orchestration, biasing routing decisions or gaining unauthorised access . - Privacy Leakage: Internal agent communication channels (e.g., inter-agent messages, shared memory, tool arguments) may expose sensitive data, even if final outputs are clean . - Observability Gaps: Without structured profile and trace instrumentation, failures are hard to attribu Internal Channel Exposure: Sensitive data may leak through inter-agent messages, shared memory, or tool arguments, which are not visible to output-only audits. Empirical studies show that internal channels can account for a significant proportion of privacy violations in multi-agent systems .

**Reference implementation:** [Lab 06](../../labs/06/README.md).

## Review answers

### Q01: What are the essential components of a reusable agent profile, and why is each important?

**Suggested answer:** - Define the concept of an agent profile in multi-agent LLM systems and articulate its role in orchestration and coordination. - Describe the architectural patterns and trade-offs involved in designing reusable agent profiles for diverse domains. - Identify the security, privacy, and reproducibility challenges associated with agent profiles, and discuss mitigation strategies. - Implement a basic reusable agent profile in Python, leverag Large Language Model (LLM) agents are rapidly evolving from isolated, single-purpose assistants into sophisticated, collaborative multi-agent systems. This progression brings new opportunities for automation, coordination, and distributed intelligence, but also introduces substantial complexity in system governance, security, and reproducibility. At the heart of these systems lies the concept of the reusable agent profile: a structured 

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: How does CapAgent achieve least-privilege delegation, and what are the trade-offs of its approa

**Suggested answer:** CapAgent encodes agent authority as a capability-constrained credential with explicit API/parameter constraints, lifecycle rules, and cross-hop provenance. This enables least-privilege multi-hop delegation with verifiable enforcement . - Agent Profile: A structured, machine-readable representation of an agent’s capabilities, constraints, identity, and provenance, designed for reuse across tasks and orchestration contexts. - Orchestration: The process of coordinating multiple agents, including task allocation, message routing, and execution monitoring. - Coordination: The mechanisms by which agents interact and collaborate to achieve shared or interdependent goals, oft

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: Why is pool-side validation necessary, and what risks arise if it is omitted ?

**Suggested answer:** This chapter explores the principles, architectures, and practicalities of engineering reusable agent profiles. We draw on contemporary research, real-world system patterns, and emerging standards, providing detailed schema examples, case studies, and hands-on lab exercises. We also address the inherent trade-offs, security risks, and open challenges that arise in this rapidly developing field. - Agent Profile: A structured, machine-readable representation of an agent’s capabilities, constraints, identity, and provenance, designed for reuse across tasks and orchestration contexts. - Orchestration: The process of coordinating multiple agents, including task allocation, message routing, and execution monitoring. - Coordination: The mechanisms by which agents interact and collaborate to achieve shared or interdependent goals, oft

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: How do agentic AIBOMs improve reproducibility and provenance compared to traditional SBOMs ?

**Suggested answer:** Runtime Drift: Profiles must capture execution context and dependency evolution to support reproducibility . Agentic AIBOMs provide structured, standards-aligned provenance artefacts that extend beyond static SBOMs. AIBOMs extend SBOMs with runtime dependency capture, environment drift monitoring, and agent decision provenance, using minimal, standards-aligned schema extensions to CycloneDX and SPDX . This allows agent profiles to serve as active provenance artefacts, supporting reproducibility and vulnerability assessment.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: Discuss the privacy risks unique to internal channels in multi-agent systems and how they can b

**Suggested answer:** Internal Channel Exposure: Sensitive data may leak through inter-agent messages, shared memory, or tool arguments, which are not visible to output-only audits. Empirical studies show that internal channels can account for a significant proportion of privacy violations in multi-agent systems . - Define the concept of an agent profile in multi-agent LLM systems and articulate its role in orchestration and coordination. - Describe the architectural patterns and trade-offs involved in designing reusable agent profiles for diverse domains. - Identify the security, privacy, and reproducibility challenges associated with agent profiles, and discuss mitigation strategies. - Implement a basic reusable agent profile in Python, leverag

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: What are the challenges in attributing failures in multi-agent LLM systems, and how do framewor

**Suggested answer:** Structured Telemetry: Frameworks such as AgentTelemetry and AgenTracer demonstrate the need for profile-linked span taxonomy and failure tracing . Without structured observability, failures are difficult to attribute, impeding system reliability. - Define the concept of an agent profile in multi-agent LLM systems and articulate its role in orchestration and coordination. - Describe the architectural patterns and trade-offs involved in designing reusable agent profiles for diverse domains. - Identify the security, privacy, and reproducibility challenges associated with agent profiles, and discuss mitigation strategies. - Implement a basic reusable agent profile in Python, leverag

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: Explain the difference between static and dynamic agent profiles, and give an example scenario 

**Suggested answer:** Scenario Example: In regulated environments (e.g., finance), static profiles may be preferable for compliance, while dynamic profiles are essential for adaptive, context-sensitive workflows. Agent profiles are not mere static descriptors. They are the foundation for dynamic delegation, trust management, and adaptive coordination. As multi-agent LLM systems scale in both size and criticality, the careful engineering of agent profiles becomes essential for:

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
