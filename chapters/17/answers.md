# Chapter 17: Worked Answers

These model-answer notes reflect textbook explanations. Open-ended tasks may admit several correct implementations.

## Applied solutions

### E01: Conceptual: Explain why increasing the number of agents in a workflow does not always improve q

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Define and distinguish between quality, cost, latency, and reliability in the context of agentic AI systems. - Identify architectural patterns and mechanisms for balancing these trade-offs in multi-agent and tool-using LLM workflows. - Explain the empirical and structural factors influencing these trade-offs, including memory, orchestration, evaluation, and guardrails. - Critically assess the limitations and open challenges in achievi Balancing quality, cost, latency, and reliability is a central challenge in the design and deployment of agentic AI systems. Architectural choices—single vs. multi-agent, static vs. adaptive routing, memory design, and guardrail integration—directly shape these trade-offs. Empirical studies reveal that more complex workflows do not always yield better outcomes and may introduce new risks or inefficiencies. Holistic evaluation, encompass

**Source-code reference:** [Lab 13](../../labs/13/README.md).

### E02: Empirical: Modify the lab code to introduce a cost budget (e.g., max 1000 tokens per task). How

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** Design Exercise - Sketch a workflow for a document summarisation task using both single-agent and multi-agent patterns. Identify points where specialisation could improve quality, and where coordination might introduce latency or cost. Trade-off Analysis - Quality: Adaptive and budgeted routing can maintain or improve quality by focusing resources where they are most needed. - Cost: Reduces unnecessary agent invocations and context expansion. - Latency: May introduce overhead for state estimation, but can avoid wasted computation. - Reliability: Sophisticated routing can improve reliability, but errors in state estimation or budget calculation may lead to missed failu

**Source-code reference:** [Lab 13](../../labs/13/README.md).

### E03: Critical Analysis: Given a scenario where user privacy is paramount, propose architectural chan

**Suggested implementation:** Write explicit access and threat assumptions, apply allowlists, and test acceptance and rejection with inspectable audit traces.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Evaluation Gaps: Many benchmarks focus on end-task accuracy, neglecting process compliance, privacy, and intermediate safety . - Memory Hallucination: Current memory systems are prone to error accumulation and hallucination, especially in long or multi-session workflows . - Guardrail Efficacy: Structural data competence, not just model scale or semantic alignment, is critical for effective guardrails; over-refusal and context-length l | Term | Definition | |---------------------|----------------------------------------------------------------------------------------------| | Agentic System | An AI system that autonomously plans, reasons, and acts, often via LLMs and tool use. | | Quality | The degree to which an agent’s outputs meet task requirements (e.g., accuracy, completeness).| | Cost | The computational, financial, or resource expenditure required to operate th

**Source-code reference:** [Lab 13](../../labs/13/README.md).

### E04: Process Evaluation: Extend the lab to log each agent’s intermediate outputs. Design a complianc

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Memory Reliability: Add a memory module that stores and retrieves previous solutions. Track hallucination rates by comparing stored outputs to ground truth. - Guardrail Integration: Implement a runtime validation step that checks for policy compliance (e.g., no use of forbidden libraries). - Budget-Constrained Execution: Enforce a maximum token budget per task, and observe the impact on quality and latency. - Process Evaluation: Log e | Term | Definition | |---------------------|----------------------------------------------------------------------------------------------| | Agentic System | An AI system that autonomously plans, reasons, and acts, often via LLMs and tool use. | | Quality | The degree to which an agent’s outputs meet task requirements (e.g., accuracy, completeness).| | Cost | The computational, financial, or resource expenditure required to operate th

**Source-code reference:** [Lab 13](../../labs/13/README.md).

### E05: Evaluation Design: Compare outcome-based and process-based evaluation for your workflow. What t

**Suggested implementation:** Define baseline, ground truth and protected holdout, record separate task success, cost, latency and process compliance, and report uncertainty.

**Validation:** normal path, invalid/unauthorized path, trace evidence and stated limitations.

**Supporting technical discussion:** - Memory Reliability: Add a memory module that stores and retrieves previous solutions. Track hallucination rates by comparing stored outputs to ground truth. - Guardrail Integration: Implement a runtime validation step that checks for policy compliance (e.g., no use of forbidden libraries). - Budget-Constrained Execution: Enforce a maximum token budget per task, and observe the impact on quality and latency. - Process Evaluation: Log e Balancing quality, cost, latency, and reliability is a central challenge in the design and deployment of agentic AI systems. Architectural choices—single vs. multi-agent, static vs. adaptive routing, memory design, and guardrail integration—directly shape these trade-offs. Empirical studies reveal that more complex workflows do not always yield better outcomes and may introduce new risks or inefficiencies. Holistic evaluation, encompass

**Source-code reference:** [Lab 13](../../labs/13/README.md).

## Review-question answers

### Q01: What are the main factors that drive the trade-off between quality and cost in agentic LLM work

**Model answer:** - Define and distinguish between quality, cost, latency, and reliability in the context of agentic AI systems. - Identify architectural patterns and mechanisms for balancing these trade-offs in multi-agent and tool-using LLM workflows. - Explain the empirical and structural factors influencing these trade-offs, including memory, orchestration, evaluation, and guardrails. - Critically assess the limitations and open challenges in achievi This chapter explores the architectural, algorithmic, and empirical foundations of these trade-offs, drawing on recent benchmarks, system designs, and evaluation frameworks. We focus on agentic workflows involving multi-agent orchestration, tool calling, memory, and runtime validation, and discuss how design choices impact the interplay between quality, cost, latency, and reliability. Throughout, we provide concrete architectural exampl

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q02: How does adaptive routing differ from static routing, and what are its advantages and limitatio

**Model answer:** - Agents: Planner, Coder, Verifier (all simulated via LLM API or local LLM). - Orchestration: Static vs. adaptive routing. - Metrics: Task success (quality), total tokens used (cost), response time (latency). - Evaluation: Process and outcome assessment. Balancing quality, cost, latency, and reliability is a central challenge in the design and deployment of agentic AI systems. Architectural choices—single vs. multi-agent, static vs. adaptive routing, memory design, and guardrail integration—directly shape these trade-offs. Empirical studies reveal that more complex workflows do not always yield better outcomes and may introduce new risks or inefficiencies. Holistic evaluation, encompass

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q03: Why is process evaluation important in agentic systems, especially in safety-critical domains?

**Model answer:** Balancing quality, cost, latency, and reliability is a central challenge in the design and deployment of agentic AI systems. Architectural choices—single vs. multi-agent, static vs. adaptive routing, memory design, and guardrail integration—directly shape these trade-offs. Empirical studies reveal that more complex workflows do not always yield better outcomes and may introduce new risks or inefficiencies. Holistic evaluation, encompass - Outcome vs. Process Evaluation: Focusing solely on final accuracy can obscure risky behaviours such as skipping critical steps or hallucinating tool use. Process evaluation, including compliance scoring and stepwise assessment, is essential for holistic reliability . - LLM Judges: LLM-as-a-judge protocols for agentic tool-calling show a structural ceiling in alignment, especially on hard queries without ground truth, and are sensitive

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q04: What empirical evidence suggests that memory systems can degrade reliability in agentic workflo

**Model answer:** - Define and distinguish between quality, cost, latency, and reliability in the context of agentic AI systems. - Identify architectural patterns and mechanisms for balancing these trade-offs in multi-agent and tool-using LLM workflows. - Explain the empirical and structural factors influencing these trade-offs, including memory, orchestration, evaluation, and guardrails. - Critically assess the limitations and open challenges in achievi This chapter explores the architectural, algorithmic, and empirical foundations of these trade-offs, drawing on recent benchmarks, system designs, and evaluation frameworks. We focus on agentic workflows involving multi-agent orchestration, tool calling, memory, and runtime validation, and discuss how design choices impact the interplay between quality, cost, latency, and reliability. Throughout, we provide concrete architectural exampl

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q05: How do guardrails and runtime validation impact the latency and cost of agentic systems?

**Model answer:** This chapter explores the architectural, algorithmic, and empirical foundations of these trade-offs, drawing on recent benchmarks, system designs, and evaluation frameworks. We focus on agentic workflows involving multi-agent orchestration, tool calling, memory, and runtime validation, and discuss how design choices impact the interplay between quality, cost, latency, and reliability. Throughout, we provide concrete architectural exampl Design Exercise - Add a runtime validation layer to a multi-agent workflow. Measure the impact on error rates, cost, and latency.

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q06: What are the limitations of using LLMs as judges for agentic tool-calling evaluation?

**Model answer:** - Outcome vs. Process Evaluation: Focusing solely on final accuracy can obscure risky behaviours such as skipping critical steps or hallucinating tool use. Process evaluation, including compliance scoring and stepwise assessment, is essential for holistic reliability . - LLM Judges: LLM-as-a-judge protocols for agentic tool-calling show a structural ceiling in alignment, especially on hard queries without ground truth, and are sensitive - Define and distinguish between quality, cost, latency, and reliability in the context of agentic AI systems. - Identify architectural patterns and mechanisms for balancing these trade-offs in multi-agent and tool-using LLM workflows. - Explain the empirical and structural factors influencing these trade-offs, including memory, orchestration, evaluation, and guardrails. - Critically assess the limitations and open challenges in achievi

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

### Q07: In what scenarios might a single-agent architecture be preferable to a multi-agent one? ---

**Model answer:** Design Exercise - Sketch a workflow for a document summarisation task using both single-agent and multi-agent patterns. Identify points where specialisation could improve quality, and where coordination might introduce latency or cost. - Define and distinguish between quality, cost, latency, and reliability in the context of agentic AI systems. - Identify architectural patterns and mechanisms for balancing these trade-offs in multi-agent and tool-using LLM workflows. - Explain the empirical and structural factors influencing these trade-offs, including memory, orchestration, evaluation, and guardrails. - Critically assess the limitations and open challenges in achievi

**Marking criteria:** correct definitions, scenario, trade-offs and bounds of evidence.

## Limits

Passing deterministic lab tests does not establish measured improvements in real LLM agent performance.
