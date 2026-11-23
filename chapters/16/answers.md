# Chapter 16: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Component Ablation: Remove the verification layer from your agent. What changes in safety and s

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Component Removal: Disabling memory, verification, or a specific agent role to observe the resulting degradation or improvement in performance. - Policy Substitution: Replacing an adaptive routing policy with a static or random policy, or vice versa . - Role Homogenisation: Using homogeneous agents (identical models and prompts) versus specialised roles (e.g., planner, executor, verifier) . - Communication Density: Varying the amount, Design an ablation experiment: Select a tool-calling agent and systematically remove (a) the memory module, (b) the verification layer, and (c) replace adaptive routing with random routing. For each ablation, hypothesise the expected impact on accuracy, cost, and safety, then implement and measure the results.

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E02: Routing Policy Swap: Implement a random routing policy that selects tools at random. Compare it

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 6. Ablation Extensions - Routing Policy Ablation: Implement a random routing policy and compare its performance to the baseline. - Memory Ablation: Add a simple memory module (e.g., store last tool call) and ablate it to assess impact on multi-turn queries. - Process Evaluation: Log the sequence of actions and analyse for risky or suboptimal behaviours. Implementing a random routing policy (selecting tools or agents at random) typically leads to degraded performance, increased cost, and higher failure rates, illustrating the necessity of informed routing policies.

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E03: Memory Ablation: Add a simple memory (e.g., store last tool call) and ablate it. Does it affect

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 6. Ablation Extensions - Routing Policy Ablation: Implement a random routing policy and compare its performance to the baseline. - Memory Ablation: Add a simple memory module (e.g., store last tool call) and ablate it to assess impact on multi-turn queries. - Process Evaluation: Log the sequence of actions and analyse for risky or suboptimal behaviours. - Component Removal: Disabling memory, verification, or a specific agent role to observe the resulting degradation or improvement in performance. - Policy Substitution: Replacing an adaptive routing policy with a static or random policy, or vice versa . - Role Homogenisation: Using homogeneous agents (identical models and prompts) versus specialised roles (e.g., planner, executor, verifier) . - Communication Density: Varying the amount,

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E04: Cost Analysis: Track token usage (if using a real LLM API). How does adding verification or mem

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Cost-Sensitive Routing: Methods such as CoSTA, ProgRouter, and STAR-O reduce token usage and compute while maintaining or improving quality . - Multi-Agent Debate: In homogeneous settings, debate increases cost without accuracy gains . - Action Routing Agents: In theorem proving, action routing can cut compute by nearly 30% without loss of performance . - Model Architecture: Single-agent vs. multi-agent, tool-calling vs. pure language, and the presence or absence of memory or verification modules. - Routing and Orchestration Policy: Static (fixed rules), adaptive (state- or progress-guided), budget-constrained, or progress-aware . - Memory System: Short-term vs. long-term, interpretable vs. opaque, constrained vs. unconstrained . - Verification and Guardrails: Presence of runtime valid

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E05: Process Evaluation: Log and analyse the sequence of actions taken by the agent. Can you identif

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** 6. Ablation Extensions - Routing Policy Ablation: Implement a random routing policy and compare its performance to the baseline. - Memory Ablation: Add a simple memory module (e.g., store last tool call) and ablate it to assess impact on multi-turn queries. - Process Evaluation: Log the sequence of actions and analyse for risky or suboptimal behaviours. - Generalisability: Ablation results are often model- and task-dependent; findings may not transfer across domains, languages, or LLM scales . - Hidden Hyperparameters: Multi-agent reinforcement learning and shared-policy training introduce implicit hyperparameters (e.g., gradient sharing) that complicate interpretation and reproducibility . - Evaluation Bottlenecks: LLM-as-a-judge protocols have structural ceilings and may not reliably

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E06: Privacy Auditing: Simulate a scenario where private information must not be disclosed to certai

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** ToolPrivacyBench demonstrates that successful tool execution does not imply appropriate privacy disclosure. Trajectory-level auditing is required to ensure that only necessary private information is transmitted to each tool . - Verifier Tax: Adding safety checks can intercept unsafe actions but may reduce overall task success and increase latency . - Privacy Guardrails: Task completion does not guarantee privacy compliance; trajectory-level auditing is required .

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

### E07: Reproducibility Challenge: Rerun your experiments with different random seeds or LLM sampling p

**Suggested implementation:** Develop a minimal validated implementation, compare it to a simpler alternative, and document operational limitations.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Attribution of Performance: It is often unclear which component or policy is responsible for observed successes or failures. - Reproducibility: Variability across runs, environments, and even random seeds can make it difficult to reproduce results. - Trade-off Measurement: Cost, quality, safety, and latency are interdependent, and architectural changes can have non-obvious effects on these metrics. - Generalisability: Ablation results are often model- and task-dependent; findings may not transfer across domains, languages, or LLM scales . - Hidden Hyperparameters: Multi-agent reinforcement learning and shared-policy training introduce implicit hyperparameters (e.g., gradient sharing) that complicate interpretation and reproducibility . - Evaluation Bottlenecks: LLM-as-a-judge protocols have structural ceilings and may not reliably

**Source-code reference:** [Lab 11](../../labs/11/README.md), [Lab 12](../../labs/12/README.md).

## Review-question answers

### Q01: What is the purpose of an ablation study in agentic LLM systems?

**Model answer:** An ablation study is a controlled experimental methodology in which specific components or features of a system are systematically removed, replaced, or altered. The goal is to assess the individual and combined contributions of these components to overall system performance. In agentic LLM systems, ablation studies are indispensable for: - Define key terminology in experimental design and architectural ablation for agentic and tool-using LLM systems. - Describe common architectures and workflow patterns for LLM agents, including single-agent, multi-agent, and tool-calling systems. - Explain the rationale and methodology behind architectural ablation studies. - Analyse trade-offs in cost, quality, safety, and reliability across different agentic architectures. - Design a

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: How does the "verifier tax" manifest in tool-using agents, and what are its implications?

**Model answer:** - Define key terminology in experimental design and architectural ablation for agentic and tool-using LLM systems. - Describe common architectures and workflow patterns for LLM agents, including single-agent, multi-agent, and tool-calling systems. - Explain the rationale and methodology behind architectural ablation studies. - Analyse trade-offs in cost, quality, safety, and reliability across different agentic architectures. - Design a - Component Removal: Disabling memory, verification, or a specific agent role to observe the resulting degradation or improvement in performance. - Policy Substitution: Replacing an adaptive routing policy with a static or random policy, or vice versa . - Role Homogenisation: Using homogeneous agents (identical models and prompts) versus specialised roles (e.g., planner, executor, verifier) . - Communication Density: Varying the amount,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: Why might multi-agent debate not outperform isolated self-correction in homogeneous teams?

**Model answer:** A controlled empirical study compared teams of homogeneous LLM agents (identical models) engaged in multi-agent debate (iteratively exchanging rationales and voting) with isolated self-correction (single agents revising their own outputs). Key findings : - Debate Failure Modes: - Sycophantic Conformity: Agents uncritically adopt majority answers, leading to modal adoption rates up to 85.5%. - Contextual Fragility: Peer rationales destabilise previously correct reasoning, with vulnerability rates up to 70%. - Consensus Collapse: Plurality voting can discard correct answers already present in the generation pool. - Cost-Accuracy Trade-off: - Debate consumed 2.1–3.4× more tokens than self-

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: What are the main trade-offs when adding runtime guardrails to an agentic workflow?

**Model answer:** - Define key terminology in experimental design and architectural ablation for agentic and tool-using LLM systems. - Describe common architectures and workflow patterns for LLM agents, including single-agent, multi-agent, and tool-calling systems. - Explain the rationale and methodology behind architectural ablation studies. - Analyse trade-offs in cost, quality, safety, and reliability across different agentic architectures. - Design a - Component Removal: Disabling memory, verification, or a specific agent role to observe the resulting degradation or improvement in performance. - Policy Substitution: Replacing an adaptive routing policy with a static or random policy, or vice versa . - Role Homogenisation: Using homogeneous agents (identical models and prompts) versus specialised roles (e.g., planner, executor, verifier) . - Communication Density: Varying the amount,

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: How can process evaluation complement outcome-based metrics in critical applications?

**Model answer:** - Model Architecture: Single-agent vs. multi-agent, tool-calling vs. pure language, and the presence or absence of memory or verification modules. - Routing and Orchestration Policy: Static (fixed rules), adaptive (state- or progress-guided), budget-constrained, or progress-aware . - Memory System: Short-term vs. long-term, interpretable vs. opaque, constrained vs. unconstrained . - Verification and Guardrails: Presence of runtime valid - Generalisability: Ablation results are often model- and task-dependent; findings may not transfer across domains, languages, or LLM scales . - Hidden Hyperparameters: Multi-agent reinforcement learning and shared-policy training introduce implicit hyperparameters (e.g., gradient sharing) that complicate interpretation and reproducibility . - Evaluation Bottlenecks: LLM-as-a-judge protocols have structural ceilings and may not reliably

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: Why is trajectory-level auditing necessary for privacy and security in multi-tool workflows?

**Model answer:** ToolPrivacyBench demonstrates that successful tool execution does not imply appropriate privacy disclosure. Trajectory-level auditing is required to ensure that only necessary private information is transmitted to each tool . - Generalisability: Ablation results are often model- and task-dependent; findings may not transfer across domains, languages, or LLM scales . - Hidden Hyperparameters: Multi-agent reinforcement learning and shared-policy training introduce implicit hyperparameters (e.g., gradient sharing) that complicate interpretation and reproducibility . - Evaluation Bottlenecks: LLM-as-a-judge protocols have structural ceilings and may not reliably

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q07: What are the limitations of LLM-as-a-judge protocols for evaluation, and how can they be mitiga

**Model answer:** - Structural Ceiling: There are fundamental limitations to LLM-as-a-judge protocols, especially on hard or ambiguous tasks. - Generalisability: Ablation results are often model- and task-dependent; findings may not transfer across domains, languages, or LLM scales . - Hidden Hyperparameters: Multi-agent reinforcement learning and shared-policy training introduce implicit hyperparameters (e.g., gradient sharing) that complicate interpretation and reproducibility . - Evaluation Bottlenecks: LLM-as-a-judge protocols have structural ceilings and may not reliably

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
