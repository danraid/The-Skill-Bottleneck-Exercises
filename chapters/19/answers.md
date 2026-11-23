# Chapter 19: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Instrument a Multi-Agent Workflow: Extend the lab outline to include a third agent and a new sk

**Suggested implementation:** Specify bounded task execution, explicit delegation rules, least-privilege profiles and failure-recovery checkpoints.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** Instrument a simple multi-agent workflow with OpenTelemetry, inject faults, and perform continuous evaluation using open-source tools. 3. Instrument Workflow - Wrap agent steps and skill invocations with OpenTelemetry spans. - Record inputs, outputs, and errors.

**Source-code reference:** [Lab 13](../../labs/13/README.md), [Lab 14](../../labs/14/README.md).

### E02: Fault Injection: Implement systematic fault injection (e.g., random skill failures, communicati

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Add a third agent (e.g., "Validator") and a new skill (e.g., "Multiplication"). - Implement systematic fault injection (e.g., random skill failures, communication drops). - Compute and plot TSR, HIR, and FDR over 100 runs with varying fault probabilities. - Log failed executions and implement a rule to refine agent behaviour (e.g., avoid division by zero). - Compare operational telemetry alone versus dual-layer (operational + reasonin - Planning Faults: Errors in task decomposition or sequencing. - Reasoning Faults: Incorrect or inconsistent internal logic. - Tool Invocation Faults: Failures in calling or executing external tools. - Delegation Faults: Errors in inter-agent communication or task assignment. - Memory Management Faults: Loss or corruption of agent state. - Safety Monitoring Faults: Failure to detect or prevent unsafe actions.

**Source-code reference:** [Lab 13](../../labs/13/README.md), [Lab 14](../../labs/14/README.md).

### E03: Metric Computation: Compute and plot Task Success Rate, Human Intervention Rate, and Fault Dete

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 6. Continuous Evaluation Loop - After each run, compute: - Task Success Rate (TSR) - Human Intervention Rate (simulate by requiring manual correction on failure) - Fault Detection Rate (FDR) 1. Human Intervention Rate (HIR): Frequency of manual corrections required. 2. Commit Failure Rate (CFR): Proportion of agent actions that break downstream pipelines. 3. Task Success Rate (TSR): Fraction of tasks completed successfully. 4. Agent Goal Achievement Reliability (AGAR): Consistency in achieving stated goals. 5. Decision Stability Metric (DSM): Variability of agent decisions across repeated runs.

**Source-code reference:** [Lab 13](../../labs/13/README.md), [Lab 14](../../labs/14/README.md).

### E04: Skill Evolution Simulation: Log failed executions and implement a simple rule to refine agent b

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Add a third agent (e.g., "Validator") and a new skill (e.g., "Multiplication"). - Implement systematic fault injection (e.g., random skill failures, communication drops). - Compute and plot TSR, HIR, and FDR over 100 runs with varying fault probabilities. - Log failed executions and implement a rule to refine agent behaviour (e.g., avoid division by zero). - Compare operational telemetry alone versus dual-layer (operational + reasonin 7. Skill Evolution (Optional) - Log failed executions. - Refine skills or agent logic based on execution feedback.

**Source-code reference:** [Lab 13](../../labs/13/README.md), [Lab 14](../../labs/14/README.md).

### E05: Observability Layer Analysis: Compare the information available from operational telemetry alon

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Add a third agent (e.g., "Validator") and a new skill (e.g., "Multiplication"). - Implement systematic fault injection (e.g., random skill failures, communication drops). - Compute and plot TSR, HIR, and FDR over 100 runs with varying fault probabilities. - Log failed executions and implement a rule to refine agent behaviour (e.g., avoid division by zero). - Compare operational telemetry alone versus dual-layer (operational + reasonin - Adaptive Reasoning Strategy Selector: Dynamically chooses between direct execution, reactive planning, or full plan-and-execute modes based on task complexity. - Hierarchical Memory System: Maintains short-term, intermediate, and long-term memories for agents, supporting context-aware reasoning and efficient retrieval. - Reliability Semantics: Explicitly defines execution guarantees for tool invocations, ensuring that actions are neit

**Source-code reference:** [Lab 13](../../labs/13/README.md), [Lab 14](../../labs/14/README.md).

## Review-question answers

### Q01: What are the main differences between observability in traditional ML systems and agentic AI sy

**Model answer:** 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc With this shift comes a new set of operational imperatives. Traditional monitoring and evaluation approaches—designed for deterministic, single-model systems—are inadequate for agentic AI, where failures may be silent, emergent, or only observable at the orchestration or business outcome level . The complexity of multi-agent workflows, the opacity of LLM reasoning, and the dynamic evolution of skill libraries all demand robust, multi-la

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: Describe the three-tier observability framework and explain why each tier is necessary.

**Model answer:** 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc - Silent and Emergent Failures: Many failures are only observable at the orchestration or business outcome level, requiring multi-layered observability and sophisticated root cause analysis . - Skill Supply Chain Security: The integration of third-party skills introduces new attack surfaces. Automated, multi-stage security analysis frameworks like ClawFuzz are necessary but not yet widespread . - Benchmark Coverage: Existing benchmarks 

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: How does the "observability tax" impact production operations, and what strategies can mitigate

**Model answer:** 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc Production operations and continuous evaluation for agentic AI systems require a paradigm shift from static, model-centric monitoring to dynamic, multi-layered, and business-aligned frameworks. By adopting distributed systems patterns, advanced observability, rigorous evaluation metrics, and continuous skill evolution, practitioners can build agentic AI pipelines that are robust, reliable, and aligned with organisational goals. However,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: What is the role of error budgets and autonomy contraction in Agent Operational Reliability Eng

**Model answer:** Agent Operational Reliability Engineering (AORE) adapts Site Reliability Engineering (SRE) practices to agentic systems, introducing two-tier service level indicators, error budgets, and autonomy contraction as enforcement actions . This balances the need for innovation and autonomy with the imperative for safety and reliability. - Error Budget: Defines the allowable threshold of errors or failures within a given period. - Autonomy Contraction: When the error budget is exceeded, agent autonomy is restricted, reducing the risk of further failures.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: Why is skill evolution important for agentic AI, and what are the main paradigms for skill eval

**Model answer:** 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc With this shift comes a new set of operational imperatives. Traditional monitoring and evaluation approaches—designed for deterministic, single-model systems—are inadequate for agentic AI, where failures may be silent, emergent, or only observable at the orchestration or business outcome level . The complexity of multi-agent workflows, the opacity of LLM reasoning, and the dynamic evolution of skill libraries all demand robust, multi-la

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: How do continuous evaluation frameworks align technical performance with business outcomes?

**Model answer:** - Telemetry Collection: Structured capture of execution traces, agent steps, tool calls, and outcomes. - Drift Detection: Monitoring for changes in data distributions or agent behaviour, which may indicate model degradation or environmental shifts. - Safety Assessment: Evaluating for unsafe, wasteful, or non-compliant actions, often using rule-based or learned policies. - Business Outcome Measurement: Correlating agent actions with busi 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q07: Give an example of a silent failure in an agentic AI system and describe how it can be detected

**Model answer:** The SPECTRA system demonstrates that only by contrasting these layers can silent failures—where the pipeline appears successful but the agent's reasoning or tool use is faulty—be reliably detected. For example, a fallback mechanism may compensate for a failed tool invocation, resulting in a superficially successful outcome that masks the underlying error. Such failures are invisible to single-layer observability tools. 1. Explain the unique operational challenges of deploying agentic AI systems in production environments. 2. Describe modern architectures and patterns for reliable, observable, and continuously evaluated agentic AI pipelines. 3. Analyse trade-offs between observability, reliability, and cost in large-scale multi-agent deployments. 4. Apply principles of continuous evaluation, including fault detection, skill evolution, and business outc

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
