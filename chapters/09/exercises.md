# Chapter 09: Engineering Reusable Agent Profiles

## Exercises

### E01

Profile Extension: Modify the schema to support runtime drift tracking (e.g., add a runtimecontext field capturing environment changes). Implement a function that compares the declared context with the current environment and flags mismatches.

### E02

Adversarial Profile Detection: Implement a pool-side validator that checks for suspicious capability declarations (e.g., excessive scope, conflicting constraints). Suggest heuristics for flagging potentially adversarial profiles.

### E03

Delegation Chain Audit: Write a function that reconstructs and visualises the delegation chain for a given agent profile. Discuss how this supports auditability and incident response.

### E04

Failure Attribution: Simulate a multi-agent workflow and use structured logs to attribute a synthetic failure to the responsible agent. Discuss how observability tooling (e.g., AgentTelemetry, AgenTracer) supports this process.

### E05

Privacy Audit: Instrument inter-agent messages and demonstrate detection of sensitive data leakage through internal channels. Propose mitigation strategies based on profile design and system instrumentation. ---

## Review questions

### Q01

What are the essential components of a reusable agent profile, and why is each important?

### Q02

How does CapAgent achieve least-privilege delegation, and what are the trade-offs of its approach ?

### Q03

Why is pool-side validation necessary, and what risks arise if it is omitted ?

### Q04

How do agentic AIBOMs improve reproducibility and provenance compared to traditional SBOMs ?

### Q05

Discuss the privacy risks unique to internal channels in multi-agent systems and how they can be mitigated .

### Q06

What are the challenges in attributing failures in multi-agent LLM systems, and how do frameworks like AgentTelemetry and AgenTracer address them ?

### Q07

Explain the difference between static and dynamic agent profiles, and give an example scenario where each is preferable. ---

## Laboratories

- [Lab 06](../../labs/06/README.md)
