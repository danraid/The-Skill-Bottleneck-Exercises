# Chapter 20: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Conceptual: Explain the difference between skill evolution and skill composition in agentic AI 

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl Skills are encapsulated procedures or tools that agents can invoke to perform specific tasks. Skill frameworks provide the structure for skill management, composition, and evolution.

**Source-code reference:** [Lab 09](../../labs/09/README.md), [Lab 14](../../labs/14/README.md).

### E02: Practical: Extend the Python lab to include a third agent (e.g., a Monitor) that observes Plann

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Add a simple skill framework: allow agents to invoke modular skills (functions). - Evaluate how skill failures propagate and are detected in traces. - Introduce a third agent (e.g., Monitor) to observe and report on Planner and Executor. def main(): steps = planner("task") try: executor(steps, injectfault=True) except Exception as e: monitor("Executor", f"Execution failed: {e}")

**Source-code reference:** [Lab 09](../../labs/09/README.md), [Lab 14](../../labs/14/README.md).

### E03: Analysis: Given a trace where an agent completes all steps but the outcome is incorrect, discus

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Use the observability tool to inject faults at specific steps (e.g., agent returns incorrect output, tool call fails). - Compare baseline and faulty executions via trace visualisation. - Operational: Detects when and where failures occur. - Accountability: Enables root cause analysis and regulatory compliance. - Reasoning: Supports debugging of agent logic and silent failure detection.

**Source-code reference:** [Lab 09](../../labs/09/README.md), [Lab 14](../../labs/14/README.md).

### E04: Critical Thinking: Discuss the trade-offs between high-fidelity observability and system perfor

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl This chapter provides a comprehensive survey of adaptive agent systems, focusing on their architectures, skill frameworks, operational patterns, and unresolved research problems. We ground our discussion in recent literature and real-world deployments, highlighting both foundational concepts and the latest developments. Special emphasis is placed on practical engineering concerns—such as observability, reliability, and security—and on t

**Source-code reference:** [Lab 09](../../labs/09/README.md), [Lab 14](../../labs/14/README.md).

### E05: Research: Propose a metric for evaluating the generalisability of a skill library across multip

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** The emergence of agentic AI systems—autonomous entities capable of perceiving goals, planning multi-step actions, interacting with complex environments, and coordinating with other agents or humans—marks a transformative advance in artificial intelligence . These systems, often powered by large language models (LLMs), are increasingly deployed across a spectrum of domains, including cloud reliability engineering , wind energy optimisati In summary, adaptive agent systems represent a transformative advance in AI, enabling autonomous, goal-directed, and collaborative behaviour across diverse domains. However, realising their full potential requires addressing deep challenges in observability, reliability, skill evolution, and security—an active and rapidly evolving research frontier.

**Source-code reference:** [Lab 09](../../labs/09/README.md), [Lab 14](../../labs/14/README.md).

## Review-question answers

### Q01: What are the main architectural differences between traditional AI agents and modern agentic AI

**Model answer:** 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl A defining characteristic of modern agentic AI is adaptivity: the capacity to adjust behaviour, acquire new skills, and reconfigure workflows in response to evolving environments, goals, or failures. This adaptivity underpins the power of agentic systems, enabling them to operate robustly in dynamic, uncertain, or adversarial settings. However, it also introduces new challenges in trust, risk, security, observability, and operational re

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: Describe the three-tier observability model for LLM-based multi-agent systems and explain why e

**Model answer:** A principled three-tier model—Operational, Accountability, Reasoning—is advocated as necessary and non-substitutable for production LLM pipelines . Each tier addresses distinct observability needs: 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: What are the limitations of static analysis in securing agent skill supply chains? How do multi

**Model answer:** - Standardising multi-layered observability and evaluation frameworks. - Developing generalisable, safe, and efficient skill ecosystems. - Advancing security analysis for agent skill supply chains, including semantic and adversarial techniques. - Improving adaptive coordination strategies under uncertainty and partial observability. - Integrating operational reliability metrics into mainstream agent evaluation and benchmarking. - Multi-stage analysis frameworks show promise, but scalable, automated enforcement is an open challenge .

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: How does operational reliability differ from correctness in the context of agentic AI? Provide 

**Model answer:** 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl Correctness—whether an agent completes a task successfully—does not guarantee operational reliability. Additional metrics are required to assess real-world performance :

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: Identify two open research problems in adaptive agent systems and outline potential approaches 

**Model answer:** 1. Define the core concepts and terminology of adaptive agent systems, especially in the context of large language model (LLM)-based multi-agent architectures. 2. Describe the architectural patterns and frameworks underpinning adaptive agentic AI systems, including skill orchestration, observability, and reliability engineering. 3. Analyse the trade-offs and challenges in deploying adaptive agent systems in real-world domains such as cl This chapter provides a comprehensive survey of adaptive agent systems, focusing on their architectures, skill frameworks, operational patterns, and unresolved research problems. We ground our discussion in recent literature and real-world deployments, highlighting both foundational concepts and the latest developments. Special emphasis is placed on practical engineering concerns—such as observability, reliability, and security—and on t

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
