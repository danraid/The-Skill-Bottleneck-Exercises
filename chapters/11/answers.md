# Chapter 11: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Delegation Chain Extension: Modify the lab code to support multi-hop delegation (e.g., Summaris

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Define Agent Roles and Capabilities - Create Python classes for agents with explicit capabilities (e.g., Summariser, Verifier, Planner). 2. Implement Delegation Chain - Use dataclasses to record each delegation step, including source, target, task, and constraints. 3. Central Orchestrator - Implement a synchronous orchestrator that: - Receives a user request. - Decomposes the task into subtasks. - Assigns subtasks to agents based on  - Credential Issuance: Authority is encoded as cryptographically protected credentials, specifying allowed APIs, parameters, and lifecycle rules. - Delegation Chain Construction: Each delegation step is recorded, forming a verifiable chain. - Verification and Auditing: Credentials are derived and verified through a layered protocol, ensuring agents cannot exceed their delegated authority.

**Reference implementation:** [Lab 09](../../labs/09/README.md).

### E02: Failure Injection: Simulate an agent failure (e.g., Verifier returns an error). Implement fallb

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Multi-Hop Delegation: Allow agents to delegate subtasks to other agents, extending the delegation chain. - Capability Constraints: Encode parameter-level constraints in agent capabilities. - Failure Handling: Simulate agent failures and implement fallback strategies. - Auditability: Implement human-readable delegation chain reporting. - Privacy Analysis: Identify sensitive data flows in the delegation chain. 1. Define Agent Roles and Capabilities - Create Python classes for agents with explicit capabilities (e.g., Summariser, Verifier, Planner). 2. Implement Delegation Chain - Use dataclasses to record each delegation step, including source, target, task, and constraints. 3. Central Orchestrator - Implement a synchronous orchestrator that: - Receives a user request. - Decomposes the task into subtasks. - Assigns subtasks to agents based on 

**Reference implementation:** [Lab 09](../../labs/09/README.md).

### E03: Capability Constraints: Extend agent capabilities to include parameter-level constraints (e.g.,

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Root Authority issues a credential to Agent A, specifying allowed actions (e.g., summarise API, input size ≤ 1000 tokens). 2. Agent A delegates a subtask to Agent B, deriving a sub-credential with stricter constraints (e.g., verify API, output length ≤ 500 words). 3. Agent B presents the credential when executing the task; the orchestrator or verifier checks the credential chain for validity and scope. 4. Revocation and Expiry: Crede - Multi-Hop Delegation: Allow agents to delegate subtasks to other agents, extending the delegation chain. - Capability Constraints: Encode parameter-level constraints in agent capabilities. - Failure Handling: Simulate agent failures and implement fallback strategies. - Auditability: Implement human-readable delegation chain reporting. - Privacy Analysis: Identify sensitive data flows in the delegation chain.

**Reference implementation:** [Lab 09](../../labs/09/README.md).

### E04: Auditability: Implement a function to print the full delegation chain in a human-readable forma

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Define Agent Roles and Capabilities - Create Python classes for agents with explicit capabilities (e.g., Summariser, Verifier, Planner). 2. Implement Delegation Chain - Use dataclasses to record each delegation step, including source, target, task, and constraints. 3. Central Orchestrator - Implement a synchronous orchestrator that: - Receives a user request. - Decomposes the task into subtasks. - Assigns subtasks to agents based on  - Multi-Hop Delegation: Allow agents to delegate subtasks to other agents, extending the delegation chain. - Capability Constraints: Encode parameter-level constraints in agent capabilities. - Failure Handling: Simulate agent failures and implement fallback strategies. - Auditability: Implement human-readable delegation chain reporting. - Privacy Analysis: Identify sensitive data flows in the delegation chain.

**Reference implementation:** [Lab 09](../../labs/09/README.md).

### E05: Privacy Analysis: Identify which parts of the delegation chain and agent outputs could leak sen

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Multi-Hop Delegation: Allow agents to delegate subtasks to other agents, extending the delegation chain. - Capability Constraints: Encode parameter-level constraints in agent capabilities. - Failure Handling: Simulate agent failures and implement fallback strategies. - Auditability: Implement human-readable delegation chain reporting. - Privacy Analysis: Identify sensitive data flows in the delegation chain. 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security.

**Reference implementation:** [Lab 09](../../labs/09/README.md).

## Review answers

### Q01: What are the main differences between orchestration, delegation, and coordination in multi-agen

**Suggested answer:** 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security. Implement a basic orchestration and delegation pipeline for a multi-agent LLM system using open-source tools, focusing on deterministic routing, delegation chain recording, and simple coordination.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: Describe the trade-offs between centralised and decentralised orchestration architectures.

**Suggested answer:** 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security. - Centralised Orchestration: Offers efficiency and control but is less robust to orchestrator failure. - Decentralised/Trustless Designs: Improve resilience and transparency but may incur higher computational and coordination overhead , .

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: How does the CapAgent framework enforce least-privilege delegation, and why is this important?

**Suggested answer:** Fine-grained delegation requires explicit encoding of agent capabilities and authority boundaries. The CapAgent framework introduces capability-constrained credentials, supporting secure, auditable delegation . - Least-Privilege Enforcement: Agents receive only the minimum authority required. - Auditability: Delegation chains support forensic analysis and compliance. - Mitigation of Lateral Movement: Prevents compromised agents from escalating privileges.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: What are the risks of relying solely on output-level audits for privacy in multi-agent systems?

**Suggested answer:** Multi-agent LLM systems introduce privacy risks via internal communication channels (inter-agent messages, shared memory, tool arguments) that are invisible to output-only audits . 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: Explain how auction-based coordination can improve decision quality in multi-agent fraud detect

**Suggested answer:** Mechanism design can be used for coordination in domains such as fraud detection. The EcoFraud framework uses an auction-based mechanism where agents submit sealed bids proportional to risk and confidence . 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: Why do multi-agent LLM systems sometimes perform worse than solo agents, even with more explora

**Suggested answer:** - Exploration vs. Discovery: Multi-agent teams may explore more but discover less, with coordination costs arising from protocol failures and impaired convergent integration . - Information Silos: Performance collapses as task complexity and agent count increase . - Fine-Grained Coordination: Agents exchange information at both agent and group levels. - Context Awareness: Semantic feedback adapts to dynamic contexts. - Accelerated Learning: Reduces exploration inefficiency in cooperative multi-agent reinforcement learning (MARL).

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: What are the limitations of prompt-driven orchestration compared to engine-orchestrated DAGs?

**Suggested answer:** Engine-orchestrated frameworks define agent interactions as explicit, deterministic workflows, often represented as directed acyclic graphs (DAGs). This approach reduces the risks of hallucinated routing and infinite loops common in prompt-driven orchestration. - Prompt-Driven Orchestration: Highly flexible but prone to hallucinated routing and non-reproducible execution. - Engine-Orchestrated DAGs: Provide deterministic, auditable workflows but may be less adaptable to open-ended tasks .

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q08: How can observability infrastructure be extended to detect agent-specific faults in orchestrati

**Suggested answer:** 1. Define the core concepts of orchestration, delegation, and coordination in multi-agent systems powered by large language models (LLMs). 2. Describe key architectural patterns and mechanisms for orchestrating LLM agents, including centralised, decentralised, and trustless designs. 3. Analyse the trade-offs between different coordination and delegation strategies, including their impact on efficiency, robustness, privacy, and security. Standard observability tools (e.g., OpenTelemetry) lack span-level representation for key agent orchestration phases such as planning, reasoning, safety monitoring, inter-agent delegation, and memory management .

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
