# Chapter 15: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Design a Multi-Step Task: Create a synthetic task that requires at least three distinct skills 

**Suggested implementation:** Distinguish persistent versus session state, isolate tenants and agents, then measure retrieval quality and failure propagation.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Select or construct a dataset with multi-step, multi-skill tasks. - Define a workflow as a sequence of steps (e.g., retrieval → reasoning → tool call → verification). - Specify required process steps and ground truth for each task. - Progress-Guided Routing: Agents select the next action or tool based on current progress, remaining difficulty, and cost constraints . For example, ProgRouter uses a multi-view progress scorer and meta-gating to dynamically select the most appropriate agent at each workflow step. - Budgeted State-Trace Routing: STAR-O formulates orchestration as a routing problem over task graphs, using compact trace states and explicit communication/

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E02: Process Evaluation: Extend the lab to record and score compliance with a prescribed process. An

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Implement compliance scoring: check if all required steps were executed in the correct order. - Analyse cases where the agent skips steps, takes shortcuts, or violates policies. - Outcome Metrics: Success rate, accuracy, and partial correctness remain important. - Process Metrics: Compliance with prescribed steps, avoidance of risky shortcuts, and adherence to privacy or safety boundaries . - Cost and Latency: Measure token usage, compute time, and latency, especially as task scale increases . - Robustness: Evaluate under adversarial, ambiguous, or multilingual conditions . - Human and LLM-as-Judge: Use both hu

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E03: Cost-Quality Trade-off: Vary the number of workflow steps and measure how token usage and laten

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Vary task complexity (e.g., number of steps, context length, number of agents). - Measure token usage, compute time, and latency for each run. - Analyse how cost and quality scale with task complexity. Sample Exercise: - Vary the number of workflow steps (e.g., add data cleaning, parameter tuning). - Measure how token usage and latency scale. - Analyse compliance scores and identify shortcutting or risky behaviour.

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E04: Memory Evaluation: Simulate a multi-session agent that must recall information from previous se

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Operation-Level Memory Evaluation: Benchmarks like HaluMem assess hallucinations and errors at each memory operation (extraction, update, QA), not just end-to-end . This enables diagnosis of where memory failures occur and how they propagate. - Multi-Session Memory Loops: MemoryArena evaluates how agents acquire, distil, and reuse memory across interdependent tasks . Agents must learn from earlier actions and feedback, distil experien - Outcome Metrics: Success rate, accuracy, and partial correctness remain important. - Process Metrics: Compliance with prescribed steps, avoidance of risky shortcuts, and adherence to privacy or safety boundaries . - Cost and Latency: Measure token usage, compute time, and latency, especially as task scale increases . - Robustness: Evaluate under adversarial, ambiguous, or multilingual conditions . - Human and LLM-as-Judge: Use both hu

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E05: LLM-as-Judge Calibration: Implement a simple LLM-as-judge protocol and compare its decisions to

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Define and contextualise "skill scalability" in agentic and tool-using AI systems. - Identify the architectural and evaluation challenges unique to benchmarking skill scalability in LLM-based agents. - Compare and contrast existing benchmarks and methodologies for evaluating agentic skill transfer, memory, tool use, and cost-quality trade-offs. - Design a principled, reproducible benchmarking protocol for skill scalability, including  - Synthetic vs. Real-World Tasks: Many benchmarks rely on synthetic or narrow tasks, which may not capture the diversity and unpredictability of real-world deployments . - Evaluation Bottlenecks: LLM-as-judge protocols can hit structural ceilings, and human annotation is costly and variable , . - Process Transparency: Automatically auditing and scoring process compliance remains challenging, especially as workflows become more complex .

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

## Review-question answers

### Q01: What are the main challenges in benchmarking skill scalability for agentic LLM systems?

**Model answer:** - Define and contextualise "skill scalability" in agentic and tool-using AI systems. - Identify the architectural and evaluation challenges unique to benchmarking skill scalability in LLM-based agents. - Compare and contrast existing benchmarks and methodologies for evaluating agentic skill transfer, memory, tool use, and cost-quality trade-offs. - Design a principled, reproducible benchmarking protocol for skill scalability, including  Skill scalability benchmarking is a cornerstone of robust, reliable agentic AI. By combining process and outcome evaluation, cost-quality analysis, and trajectory-level auditing, researchers and practitioners can better diagnose, compare, and improve agentic systems as they scale to real-world complexity. The field remains fast-moving, with open challenges in evaluation, memory, privacy, and cross-domain generalisation. This chapter pro

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: How does process evaluation differ from traditional outcome-based evaluation, and why is it imp

**Model answer:** - Outcome Metrics: Success rate, accuracy, and partial correctness remain important. - Process Metrics: Compliance with prescribed steps, avoidance of risky shortcuts, and adherence to privacy or safety boundaries . - Cost and Latency: Measure token usage, compute time, and latency, especially as task scale increases . - Robustness: Evaluate under adversarial, ambiguous, or multilingual conditions . - Human and LLM-as-Judge: Use both hu - Define and contextualise "skill scalability" in agentic and tool-using AI systems. - Identify the architectural and evaluation challenges unique to benchmarking skill scalability in LLM-based agents. - Compare and contrast existing benchmarks and methodologies for evaluating agentic skill transfer, memory, tool use, and cost-quality trade-offs. - Design a principled, reproducible benchmarking protocol for skill scalability, including 

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: Describe two methods for balancing cost and quality in multi-agent workflows.

**Model answer:** - Token and Compute Overhead: Multi-agent debate, verification, and long-horizon workflows can multiply token usage and latency , . For example, peer debate may consume 2.1–3.4× more tokens than isolated self-correction, with equal or lower accuracy. - Verifier Tax: Adding runtime safety checks can reduce unsafe actions but may not guarantee safe completion and can increase cost . Safety mediation can intercept non-compliant actions but - Progress-Guided Routing: Agents select the next action or tool based on current progress, remaining difficulty, and cost constraints . For example, ProgRouter uses a multi-view progress scorer and meta-gating to dynamically select the most appropriate agent at each workflow step. - Budgeted State-Trace Routing: STAR-O formulates orchestration as a routing problem over task graphs, using compact trace states and explicit communication/

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: What are the risks of relying solely on LLM-as-judge evaluation, and how can they be mitigated?

**Model answer:** - Operation-Level Memory Evaluation: Benchmarks like HaluMem assess hallucinations and errors at each memory operation (extraction, update, QA), not just end-to-end . This enables diagnosis of where memory failures occur and how they propagate. - Multi-Session Memory Loops: MemoryArena evaluates how agents acquire, distil, and reuse memory across interdependent tasks . Agents must learn from earlier actions and feedback, distil experien - Outcome Metrics: Success rate, accuracy, and partial correctness remain important. - Process Metrics: Compliance with prescribed steps, avoidance of risky shortcuts, and adherence to privacy or safety boundaries . - Cost and Latency: Measure token usage, compute time, and latency, especially as task scale increases . - Robustness: Evaluate under adversarial, ambiguous, or multilingual conditions . - Human and LLM-as-Judge: Use both hu

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: How does memory reliability affect skill scalability in long-horizon tasks?

**Model answer:** - Synthetic vs. Real-World Tasks: Many benchmarks rely on synthetic or narrow tasks, which may not capture the diversity and unpredictability of real-world deployments . - Evaluation Bottlenecks: LLM-as-judge protocols can hit structural ceilings, and human annotation is costly and variable , . - Process Transparency: Automatically auditing and scoring process compliance remains challenging, especially as workflows become more complex . The rapid evolution of large language models (LLMs) from static text generators to agentic systems—capable of planning, tool use, and multi-step reasoning—has foregrounded the concept of skill scalability. This refers to an agent’s ability to generalise, transfer, and compose skills as tasks increase in complexity, length, or diversity . In practical deployments, agents must not only solve isolated tasks but also adapt and maintain reli

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: Why is trajectory-level auditing necessary for privacy and safety in tool-using agents? ---

**Model answer:** - Continuous Validation: Embedding claim extraction, retrieval-based grounding, and policy enforcement into the execution lifecycle improves reliability . This validation layer screens outputs before execution, reducing error propagation. - Trajectory-Level Guardrails: TraceSafe-Bench audits not just final outputs but the entire tool-calling trajectory for safety and compliance . Structural competence (e.g., correct JSON parsing) often  - Developing more realistic, diverse, and process-aware benchmarks. - Improving memory and verification mechanisms for long-horizon and multi-session tasks. - Advancing hybrid human-LLM evaluation protocols that are both scalable and reliable. - Integrating trajectory-level auditing for privacy and safety into standard evaluation pipelines. - Addressing cross-lingual and multi-modal benchmarking gaps to ensure equitable and robust agent

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
