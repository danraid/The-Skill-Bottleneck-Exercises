# Chapter 01: The Agent Capability Paradox

## Practical exercises

### E01

Extend the Tool Registry: Add multiplication and division tools. Update the intent classifier accordingly.

### E02

Implement Trust Decay: Modify the trust scoring so that recent failures decrease a tool’s score more than old failures.

### E03

Simulate Prompt Injection: Add a “malicious” tool to the registry. Write a function that simulates a prompt injection attack by manipulating the intent classifier to always select the malicious tool.

### E04

Context Window Simulation: Simulate a context window limit by restricting the number of tokens (words) the agent can process. Observe how this affects tool selection and workflow.

### E05

Logging Enhancements: Add structured logging to record every decision, tool invocation, and error for later analysis. ---

## Review questions

### Q01

What is the difference between an AI agent and agentic AI?

### Q02

Why does increasing agent capability sometimes reduce reliability or transparency?

### Q03

Describe the lost-in-the-middle effect and its implications for long-context reasoning.

### Q04

How can runtime trust scoring improve tool selection in agentic AI?

### Q05

What are the main security risks associated with agentic tool use?

### Q06

Explain how hierarchical agent architectures can automate complex workflows. ---

## Reference laboratories

- [Lab 01](../../labs/01/README.md)
