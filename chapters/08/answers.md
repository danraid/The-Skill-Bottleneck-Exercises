# Chapter 08: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Role Expansion: Add a Compliance subagent that checks whether retrieved information adheres to 

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Modularity and Maintainability: Each subagent can be developed, tested, and improved independently, supporting rapid iteration and domain extension . - Role Specialisation: Agents can be tailored for distinct functions such as planning, retrieval, verification, actuation, or compliance . - Scalability: Tasks can be distributed across agents, enabling parallelism and more efficient resource utilisation . - Improved Traceability: Explic - Planner: Decomposes high-level goals into subtasks and allocates them to suitable agents. - Retriever: Gathers relevant information or documents from internal or external sources. - Verifier: Checks outputs for correctness, compliance, or completeness. - Executor: Performs actions in the environment or invokes external tools. - Memory Manager: Maintains and shares context, evidence, or intermediate results . - Security/Compliance Agen

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E02: Failure Simulation: Inject a failure into the Retriever and implement fallback handling in the 

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Define Agent Roles: Implement at least three subagents (e.g., Planner, Retriever, Verifier), each as a Python class with a handle method. 2. Implement Orchestrator: The orchestrator receives a user query, decomposes it into subtasks, and delegates each to the appropriate subagent. 3. Communication Protocols: Support both natural language (string-based) and structured (dictionary-based) message passing between orchestrator and subagen - Implement structured graph-based message passing (e.g., using adjacency lists or dictionaries to represent dependencies). - Add error handling and recovery logic in the orchestrator. - Compare with a monolithic agent (a single class handling all steps). - Add a Compliance subagent for policy checks. - Implement a simple capability chain for delegation and verify authorisation.

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E03: Memory Analysis: Modify the MemoryBank to support section-level evidence storage as in ADORE .

**Suggested approach:** Implement progressive metadata/body disclosure with strict context and state boundaries; evaluate recall and context usage.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** 1. Define Agent Roles: Implement at least three subagents (e.g., Planner, Retriever, Verifier), each as a Python class with a handle method. 2. Implement Orchestrator: The orchestrator receives a user query, decomposes it into subtasks, and delegates each to the appropriate subagent. 3. Communication Protocols: Support both natural language (string-based) and structured (dictionary-based) message passing between orchestrator and subagen - Structured Logging: All agent interactions, decisions, and state transitions should be logged with unique identifiers and timestamps. - Trace Replay: Systems should support replaying execution traces for post-mortem analysis. - Span Taxonomies: Observability frameworks should define span kinds for planning, reasoning, delegation, memory management, and tool execution.

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E04: Coordination Cost Measurement: Measure the number of messages and steps required in both monoli

**Suggested approach:** Design controlled evaluation against baseline, ground truth and held-out tasks; report outcome, latency and cost separately.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Context Window Constraints: LLMs have finite context windows, making it difficult to process large or complex tasks in a single pass. This limits the agent's ability to maintain long-term state or reason over extensive evidence . - Lack of Modularity: All capabilities are entangled within a single model, making debugging, extension, and maintenance challenging. Any change or failure can have unpredictable system-wide effects. - Poor S 1. Define Agent Roles: Implement at least three subagents (e.g., Planner, Retriever, Verifier), each as a Python class with a handle method. 2. Implement Orchestrator: The orchestrator receives a user query, decomposes it into subtasks, and delegates each to the appropriate subagent. 3. Communication Protocols: Support both natural language (string-based) and structured (dictionary-based) message passing between orchestrator and subagen

**Reference implementation:** [Lab 06](../../labs/06/README.md).

### E05: Security Extension: Implement a simple capability chain for delegation and verify that only aut

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Monolithic Agent: A single, unified AI agent responsible for all aspects of a task, including perception, reasoning, planning, and action. - Subagent: A specialised component within a multi-agent system, typically responsible for a specific subtask or function. - Orchestrator: A central or distributed controller that coordinates the activities of multiple subagents. - Delegation: The process by which one agent assigns a subtask to ano - Implement structured graph-based message passing (e.g., using adjacency lists or dictionaries to represent dependencies). - Add error handling and recovery logic in the orchestrator. - Compare with a monolithic agent (a single class handling all steps). - Add a Compliance subagent for policy checks. - Implement a simple capability chain for delegation and verify authorisation.

**Reference implementation:** [Lab 06](../../labs/06/README.md).

## Review answers

### Q01: What are the main limitations of monolithic LLM agents in complex, real-world tasks?

**Suggested answer:** The field of artificial intelligence has undergone a significant transformation with the emergence of large language models (LLMs) as general-purpose agents. Early LLM-based systems were typically monolithic: a single model instance was responsible for all aspects of perception, reasoning, planning, and action. However, as the complexity and scale of real-world tasks have grown, the limitations of this approach have become increasingly  - Context Window Constraints: LLMs have finite context windows, making it difficult to process large or complex tasks in a single pass. This limits the agent's ability to maintain long-term state or reason over extensive evidence . - Lack of Modularity: All capabilities are entangled within a single model, making debugging, extension, and maintenance challenging. Any change or failure can have unpredictable system-wide effects. - Poor S

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: How does explicit task decomposition into specialised subagents improve modularity and traceabi

**Suggested answer:** 1. Distinguish between monolithic and multi-agent (specialised subagent) architectures in LLM-based systems. 2. Explain the motivations and theoretical underpinnings for decomposing agentic systems into specialised subagents. 3. Describe key architectural patterns, coordination mechanisms, and memory models for orchestrating specialised agents. 4. Evaluate the trade-offs, limitations, and security implications of multi-agent orchestrati The transition from monolithic agents to specialised subagents in LLM-based systems is motivated by the need for modularity, scalability, and robustness in complex, real-world applications. Multi-agent architectures enable explicit role specialisation, parallelism, and fine-grained control, but introduce new challenges in coordination, security, observability, and governance. Addressing these challenges requires careful architectural de

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: What are the trade-offs between natural language and structured graph-based communication in mu

**Suggested answer:** Design and implement a simple multi-agent orchestration system in Python, where a central orchestrator delegates subtasks to specialised subagents. The system should support both natural language and structured graph-based communication, shared memory, and basic fault injection. 1. Define Agent Roles: Implement at least three subagents (e.g., Planner, Retriever, Verifier), each as a Python class with a handle method. 2. Implement Orchestrator: The orchestrator receives a user query, decomposes it into subtasks, and delegates each to the appropriate subagent. 3. Communication Protocols: Support both natural language (string-based) and structured (dictionary-based) message passing between orchestrator and subagen

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: Describe one coordination mechanism that can be used to resolve conflicting recommendations amo

**Suggested answer:** - Monolithic Agent: A single, unified AI agent responsible for all aspects of a task, including perception, reasoning, planning, and action. - Subagent: A specialised component within a multi-agent system, typically responsible for a specific subtask or function. - Orchestrator: A central or distributed controller that coordinates the activities of multiple subagents. - Delegation: The process by which one agent assigns a subtask to ano 1. Distinguish between monolithic and multi-agent (specialised subagent) architectures in LLM-based systems. 2. Explain the motivations and theoretical underpinnings for decomposing agentic systems into specialised subagents. 3. Describe key architectural patterns, coordination mechanisms, and memory models for orchestrating specialised agents. 4. Evaluate the trade-offs, limitations, and security implications of multi-agent orchestrati

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: What security and privacy risks are unique to multi-agent LLM systems compared to monolithic ag

**Suggested answer:** 1. Distinguish between monolithic and multi-agent (specialised subagent) architectures in LLM-based systems. 2. Explain the motivations and theoretical underpinnings for decomposing agentic systems into specialised subagents. 3. Describe key architectural patterns, coordination mechanisms, and memory models for orchestrating specialised agents. 4. Evaluate the trade-offs, limitations, and security implications of multi-agent orchestrati - Monolithic Agent: A single, unified AI agent responsible for all aspects of a task, including perception, reasoning, planning, and action. - Subagent: A specialised component within a multi-agent system, typically responsible for a specific subtask or function. - Orchestrator: A central or distributed controller that coordinates the activities of multiple subagents. - Delegation: The process by which one agent assigns a subtask to ano

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: How can failure attribution be improved in multi-agent orchestration frameworks?

**Suggested answer:** - Failure Attribution: Pinpointing which agent or step caused a failure is challenging; specialised tracing frameworks are required . - Tool-Use Hallucination: Diagnosing and attributing tool-use errors requires stage-level benchmarks and composite metrics . 1. Distinguish between monolithic and multi-agent (specialised subagent) architectures in LLM-based systems. 2. Explain the motivations and theoretical underpinnings for decomposing agentic systems into specialised subagents. 3. Describe key architectural patterns, coordination mechanisms, and memory models for orchestrating specialised agents. 4. Evaluate the trade-offs, limitations, and security implications of multi-agent orchestrati

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: Explain the concept of the autonomy paradox in ethical multi-agent coordination. ---

**Suggested answer:** 1. Distinguish between monolithic and multi-agent (specialised subagent) architectures in LLM-based systems. 2. Explain the motivations and theoretical underpinnings for decomposing agentic systems into specialised subagents. 3. Describe key architectural patterns, coordination mechanisms, and memory models for orchestrating specialised agents. 4. Evaluate the trade-offs, limitations, and security implications of multi-agent orchestrati - Monolithic Agent: A single, unified AI agent responsible for all aspects of a task, including perception, reasoning, planning, and action. - Subagent: A specialised component within a multi-agent system, typically responsible for a specific subtask or function. - Orchestrator: A central or distributed controller that coordinates the activities of multiple subagents. - Delegation: The process by which one agent assigns a subtask to ano

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
