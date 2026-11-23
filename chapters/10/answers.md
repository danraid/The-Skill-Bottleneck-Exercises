# Chapter 10: Worked Answers

These pedagogical model-answer notes are based on the source chapter. Different designs may satisfy open-ended exercises.

## Practical solutions

### E01: Playbook Extension: Modify the playbook to include a conditional branch: if the verifier reject

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** python playbook = [ {"id": "step1", "agent": "summariser", "inputkeys": ["document"], "outputkey": "summary", "deps": []}, {"id": "step2", "agent": "qa", "inputkeys": ["summary", "question"], "outputkey": "answer", "deps": ["step1"]}, {"id": "step3", "agent": "verifier", "inputkeys": ["answer"], "outputkey": "verdict", "deps": ["step2"]}, ] - Deterministic Routing: The orchestrator follows a predefined plan, ensuring that the same inputs yield the same execution trace. - Parallelism and Conditional Control: Explicit DAGs support parallel execution of independent branches and conditional transitions based on structured state predicates . - Auditability: Execution traces can be logged, replayed, and audited, supporting compliance and debugging. - Isolation of Context: Memory

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E02: Parallel Execution: Adapt the orchestrator to execute independent steps in parallel using Pytho

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Adapt the orchestrator to execute independent steps in parallel using Python's concurrent.futures. - Deterministic Routing: The orchestrator follows a predefined plan, ensuring that the same inputs yield the same execution trace. - Parallelism and Conditional Control: Explicit DAGs support parallel execution of independent branches and conditional transitions based on structured state predicates . - Auditability: Execution traces can be logged, replayed, and audited, supporting compliance and debugging. - Isolation of Context: Memory

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E03: Structured State: Implement a structured state object that separates ephemeral, persistent, and

**Suggested approach:** Implement a minimal, deterministic example, test success and failure cases, and explain assumptions and limitations.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Ephemeral Scratch Space: Temporary data relevant only within a single step or branch. - Structured State: Persistent, structured data shared across steps, such as intermediate results or agent outputs. - External Connectors: Interfaces to databases, APIs, or external systems, supporting integration and long-term storage. - Playbook Definition: The workflow is encoded as a DAG or similar structure, specifying agent roles, dependencies, and transitions. - Orchestrator Engine: A deterministic engine interprets the playbook, manages state, and invokes agents as typed functions . - Agent Pool: A set of agents, each with well-defined capabilities and interfaces. - Memory Tiers: Multi-level memory (e.g., ephemeral scratch space, structured state, external conn

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E04: Failure Attribution: Instrument the orchestrator to log which agent or step fails, and suggest 

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Playbook Definition: The workflow is encoded as a DAG or similar structure, specifying agent roles, dependencies, and transitions. - Orchestrator Engine: A deterministic engine interprets the playbook, manages state, and invokes agents as typed functions . - Agent Pool: A set of agents, each with well-defined capabilities and interfaces. - Memory Tiers: Multi-level memory (e.g., ephemeral scratch space, structured state, external conn Instrument a playbook-driven orchestrator to log span-level events for each orchestration phase. Analyse a failure trace and attribute the root cause to a specific agent or step.

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E05: Hybrid Delegation: Implement a router that chooses between structured and natural language dele

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Hybrid approaches, such as Routed Graph Handoff, use lightweight routers to select between structured graphs and natural language delegation for each step, balancing cost and capability . Implement a router that selects between structured and natural language delegation for each step in a workflow, based on task complexity and agent capability.

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E06: Automated Playbook Synthesis: Write a function that takes a natural language task description a

**Suggested approach:** Build an explicit task DAG with specialist roles, tool permissions and bounded retries; verify delegation traces and error handling.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** Design an algorithm that takes a natural language task description and synthesises a playbook DAG, mapping subtasks to available agents. Discuss how you would validate the correctness and completeness of the generated playbook. Implement a router that selects between structured and natural language delegation for each step in a workflow, based on task complexity and agent capability.

**Reference implementation:** [Lab 07](../../labs/07/README.md).

### E07: Security Layer: Integrate capability-based delegation into the orchestrator, ensuring that each

**Suggested approach:** Use an explicit allowlist and structured tool schema, reject untrusted instructions or malformed requests, and collect trace evidence.

**Acceptance criteria:** expected result, failure rejection, auditability, documented trade-offs.

**Textbook-based rationale:** - Playbook Definition: The workflow is encoded as a DAG or similar structure, specifying agent roles, dependencies, and transitions. - Orchestrator Engine: A deterministic engine interprets the playbook, manages state, and invokes agents as typed functions . - Agent Pool: A set of agents, each with well-defined capabilities and interfaces. - Memory Tiers: Multi-level memory (e.g., ephemeral scratch space, structured state, external conn - Deterministic Routing: The orchestrator follows a predefined plan, ensuring that the same inputs yield the same execution trace. - Parallelism and Conditional Control: Explicit DAGs support parallel execution of independent branches and conditional transitions based on structured state predicates . - Auditability: Execution traces can be logged, replayed, and audited, supporting compliance and debugging. - Isolation of Context: Memory

**Reference implementation:** [Lab 07](../../labs/07/README.md).

## Review answers

### Q01: What are the main advantages of playbook-driven agent execution over prompted orchestration?

**Suggested answer:** - Define and distinguish playbook-driven agent execution from prompted and ad hoc orchestration. - Describe the architectural components and workflows of playbook-driven multi-agent systems. - Analyse the trade-offs between deterministic, playbook-based orchestration and dynamic, language-driven coordination. - Identify security, privacy, and reliability challenges in multi-agent agentic systems, and explain how playbook-driven approach Playbook-driven agent execution represents a significant step toward robust, reproducible, and auditable multi-agent systems. By externalising workflow control, separating memory, and constraining agent actions to explicit plans, these systems address many pitfalls of prompted orchestration. However, challenges remain in adaptability, scalability, security, and effective distributed reasoning. As the field evolves, hybrid architectures,

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q02: How does explicit memory architecture contribute to reliability and performance in agentic syst

**Suggested answer:** GraphBit exemplifies this architecture by defining workflows as explicit DAGs, with a Rust-based engine governing routing and state transitions. Agents are invoked as typed functions, and the engine supports parallel branches, conditional control, and error recovery. A three-tier memory architecture isolates context, preventing cascading context bloat . Playbook-driven agent execution represents a significant step toward robust, reproducible, and auditable multi-agent systems. By externalising workflow control, separating memory, and constraining agent actions to explicit plans, these systems address many pitfalls of prompted orchestration. However, challenges remain in adaptability, scalability, security, and effective distributed reasoning. As the field evolves, hybrid architectures,

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q03: What are the trade-offs between deterministic and dynamic orchestration in multi-agent workflow

**Suggested answer:** - Define and distinguish playbook-driven agent execution from prompted and ad hoc orchestration. - Describe the architectural components and workflows of playbook-driven multi-agent systems. - Analyse the trade-offs between deterministic, playbook-based orchestration and dynamic, language-driven coordination. - Identify security, privacy, and reliability challenges in multi-agent agentic systems, and explain how playbook-driven approach - Deterministic Playbooks: Ensure reproducibility and auditability, but may struggle with highly dynamic or underspecified tasks. - Prompted/Dynamic Orchestration: Offers flexibility and adaptability, but at the cost of reproducibility and reliability.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q04: How do playbook-driven systems address tool-use hallucination and failure attribution?

**Suggested answer:** - Tool-Use Hallucination: Playbook-driven execution can reduce tool-use hallucination by constraining agent actions to predefined steps, but failures can still propagate across judgment, planning, and execution stages . - Stage-Level Attribution: Benchmarks like Agent-Trident enable fine-grained diagnosis of tool-use failures, supporting safer deployment. - Non-determinism: The same prompt may yield different execution paths on repeated runs, making debugging and reproducibility difficult . - Hallucinated Routing: LLMs may invent non-existent modules, skip required steps, or enter infinite loops, especially in tool-intensive or long-running pipelines . - Context Bloat: As workflows grow, maintaining all relevant context in the prompt becomes infeasible, leading to degraded reasoning and 

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q05: What security and privacy risks are introduced by centralised orchestrators, and how can they b

**Suggested answer:** - Non-determinism: The same prompt may yield different execution paths on repeated runs, making debugging and reproducibility difficult . - Hallucinated Routing: LLMs may invent non-existent modules, skip required steps, or enter infinite loops, especially in tool-intensive or long-running pipelines . - Context Bloat: As workflows grow, maintaining all relevant context in the prompt becomes infeasible, leading to degraded reasoning and  - Define and distinguish playbook-driven agent execution from prompted and ad hoc orchestration. - Describe the architectural components and workflows of playbook-driven multi-agent systems. - Analyse the trade-offs between deterministic, playbook-based orchestration and dynamic, language-driven coordination. - Identify security, privacy, and reliability challenges in multi-agent agentic systems, and explain how playbook-driven approach

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q06: How does evidence-driven execution improve robustness in multi-agent workflows?

**Suggested answer:** - Define and distinguish playbook-driven agent execution from prompted and ad hoc orchestration. - Describe the architectural components and workflows of playbook-driven multi-agent systems. - Analyse the trade-offs between deterministic, playbook-based orchestration and dynamic, language-driven coordination. - Identify security, privacy, and reliability challenges in multi-agent agentic systems, and explain how playbook-driven approach As Large Language Model (LLM) agents become increasingly central to complex, real-world workflows, the demand for robust, reproducible, and auditable orchestration intensifies. Early agentic systems often relied on prompted orchestration, in which the LLM itself determines the next step in a workflow based on natural language instructions and the current context. While this approach offers flexibility, it is prone to hallucinated routin

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q07: What are the challenges of automated playbook synthesis and modularisation?

**Suggested answer:** Automated playbook synthesis and modularisation are emerging research areas. Systems may use LLMs to generate or adapt playbooks based on high-level objectives, decomposing complex tasks into reusable modules. However, challenges remain in ensuring correctness, composability, and security. As workflows grow, playbooks can become large and difficult to maintain. Automated playbook synthesis and modularisation are promising directions, but remain underexplored. Ensuring correctness, composability, and security in automatically generated playbooks is a significant challenge.

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

### Q08: How can hybrid orchestration models balance flexibility and reproducibility? ---

**Suggested answer:** - Deterministic Playbooks: Ensure reproducibility and auditability, but may struggle with highly dynamic or underspecified tasks. - Prompted/Dynamic Orchestration: Offers flexibility and adaptability, but at the cost of reproducibility and reliability. As Large Language Model (LLM) agents become increasingly central to complex, real-world workflows, the demand for robust, reproducible, and auditable orchestration intensifies. Early agentic systems often relied on prompted orchestration, in which the LLM itself determines the next step in a workflow based on natural language instructions and the current context. While this approach offers flexibility, it is prone to hallucinated routin

**Evaluation criteria:** conceptual precision, example, trade-off and limitations.

## Evidence scope

Offline educational tests are not real model benchmarks or evidence of production-grade security.
