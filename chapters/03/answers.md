# Chapter 03: Worked Answers

The reference responses are based on the corresponding chapter. Open-ended assignments can admit multiple correct designs.

## Exercise solutions

### E01: Conceptual: Explain the difference between context window saturation and semantic competition a

**Reference approach:** Separate discovery metadata from detailed tool instructions, measure context exposed, and test retrieval and information-isolation edge cases.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Define cognitive and contextual bottlenecks in agentic AI and LLM-based agent systems. - Describe the architectural and operational sources of these bottlenecks, including context window limitations, semantic competition, and reasoning depth. - Analyse the impact of bottlenecks on tool selection, task execution, and reliability in agentic AI. - Evaluate current strategies and frameworks for mitigating cognitive and contextua - Cognitive bottlenecks: Limitations in reasoning, memory, and self-assessment that restrict the agent’s ability to plan, integrate evidence, and adapt to complex tasks. - Contextual bottlenecks: Constraints imposed by the architecture, such as the finite context window, position bias, and semantic competition, which hinder the agent’s ability to process, retrieve, and act upon relevant information.

**Reference code:** [Lab 03](../../labs/03/README.md).

### E02: Practical: Modify the Python lab to simulate the lost-in-the-middle effect by placing the corre

**Reference approach:** Construct a baseline and ground-truth tasks, separate development and protected confirmation splits, and report quality, latency, cost and uncertainties independently.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Simulate Lost-in-the-Middle: Place the correct tool’s metadata in the middle of the prompt and measure selection accuracy. - Vary Metadata Fields: Systematically test the impact of including/excluding descriptions and schemas. - Agentic AI: Systems exhibiting autonomous, adaptive workflow control, including dynamic tool selection and multi-step reasoning, often orchestrated by LLMs . - AI Agent: A modular system, often LLM-driven, that automates specific tasks through tool integration and prompt engineering . - Context Window: The maximum number of tokens (words or subwords) an LLM can process at once. - Lost-in-the-Middle (LitM): A phenomenon where

**Reference code:** [Lab 03](../../labs/03/README.md).

### E03: Critical Analysis: Discuss how trust-aware tool selection frameworks can mitigate reliability b

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Define cognitive and contextual bottlenecks in agentic AI and LLM-based agent systems. - Describe the architectural and operational sources of these bottlenecks, including context window limitations, semantic competition, and reasoning depth. - Analyse the impact of bottlenecks on tool selection, task execution, and reliability in agentic AI. - Evaluate current strategies and frameworks for mitigating cognitive and contextua - Metadata Overload: Including detailed tool descriptions, schemas, and usage examples can quickly exhaust the context window. - Semantic Routing: The agent must interpret tool names, descriptions, and schemas to route requests accurately. Studies show that qualified tool names often encode sufficient semantic information for effective routing, while descriptions become more useful only in larger models (>7B parameters) . - Tr

**Reference code:** [Lab 03](../../labs/03/README.md).

### E04: Research: Summarise the main findings of regarding evidence scope, dispersion, and reasoning de

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Agentic AI: Systems exhibiting autonomous, adaptive workflow control, including dynamic tool selection and multi-step reasoning, often orchestrated by LLMs . - AI Agent: A modular system, often LLM-driven, that automates specific tasks through tool integration and prompt engineering . - Context Window: The maximum number of tokens (words or subwords) an LLM can process at once. - Lost-in-the-Middle (LitM): A phenomenon where - Evidence Scope: The quantity of information that must be located and processed. - Evidence Dispersion: The degree to which necessary information is scattered throughout the context. - Reasoning Depth: The number of dependent inferential steps required to reach an answer.

**Reference code:** [Lab 03](../../labs/03/README.md).

### E05: Security: Describe a prompt injection attack on tool selection and outline a basic defence mech

**Reference approach:** Define trusted versus untrusted inputs, a tool allowlist and an explicit unauthorized-call denial case; record a structured audit trace.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Agentic AI: Systems exhibiting autonomous, adaptive workflow control, including dynamic tool selection and multi-step reasoning, often orchestrated by LLMs . - AI Agent: A modular system, often LLM-driven, that automates specific tasks through tool integration and prompt engineering . - Context Window: The maximum number of tokens (words or subwords) an LLM can process at once. - Lost-in-the-Middle (LitM): A phenomenon where - Architectural Constraints: LitM and position bias are deeply rooted in transformer design and are not fully addressed by current mitigation strategies . - Scalability: As tool registries grow, context window and semantic routing bottlenecks become more pronounced, challenging existing orchestration frameworks . - Security: Prompt injection and tool hijacking attacks remain an unsolved threat in open tool ecosystems . - Gener

**Reference code:** [Lab 03](../../labs/03/README.md).

## Review-question answers

### Q01: What is the "lost-in-the-middle" phenomenon, and why does it persist even after model training?

**Answer notes:** - Lost-in-the-middle is rooted in transformer architecture and is not fully mitigated by standard training or positional encoding modifications . - Semantic competition remains a challenge in RAG systems, even when context length is controlled . - Agentic AI: Systems exhibiting autonomous, adaptive workflow control, including dynamic tool selection and multi-step reasoning, often orchestrated by LLMs . - AI Agent: A modular system, often LLM-driven, that automates specific tasks through tool integration and prompt engineering . - Context Window: The maximum number of tokens (words or subwords) an LLM can process at once. - Lost-in-the-Middle (LitM): A phenomenon where

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q02: How does semantic competition differ from context length in affecting retrieval-augmented gener

**Answer notes:** Retrieval-augmented generation (RAG) systems often fail not solely due to long context length, but because of semantic competition—when multiple passages appear relevant, making it difficult for the model to identify the correct one . Controlled experiments demonstrate: - Define cognitive and contextual bottlenecks in agentic AI and LLM-based agent systems. - Describe the architectural and operational sources of these bottlenecks, including context window limitations, semantic competition, and reasoning depth. - Analyse the impact of bottlenecks on tool selection, task execution, and reliability in agentic AI. - Evaluate current strategies and frameworks for mitigating cognitive and contextua

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q03: Why is dynamic tool selection both a strength and a vulnerability in agentic AI systems?

**Answer notes:** - Agentic AI: Systems exhibiting autonomous, adaptive workflow control, including dynamic tool selection and multi-step reasoning, often orchestrated by LLMs . - AI Agent: A modular system, often LLM-driven, that automates specific tasks through tool integration and prompt engineering . - Context Window: The maximum number of tokens (words or subwords) an LLM can process at once. - Lost-in-the-Middle (LitM): A phenomenon where - Define cognitive and contextual bottlenecks in agentic AI and LLM-based agent systems. - Describe the architectural and operational sources of these bottlenecks, including context window limitations, semantic competition, and reasoning depth. - Analyse the impact of bottlenecks on tool selection, task execution, and reliability in agentic AI. - Evaluate current strategies and frameworks for mitigating cognitive and contextua

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q04: What architectural innovations have been proposed to improve scalability and generalisation in 

**Answer notes:** - Architectural Constraints: LitM and position bias are deeply rooted in transformer design and are not fully addressed by current mitigation strategies . - Scalability: As tool registries grow, context window and semantic routing bottlenecks become more pronounced, challenging existing orchestration frameworks . - Security: Prompt injection and tool hijacking attacks remain an unsolved threat in open tool ecosystems . - Gener - Define cognitive and contextual bottlenecks in agentic AI and LLM-based agent systems. - Describe the architectural and operational sources of these bottlenecks, including context window limitations, semantic competition, and reasoning depth. - Analyse the impact of bottlenecks on tool selection, task execution, and reliability in agentic AI. - Evaluate current strategies and frameworks for mitigating cognitive and contextua

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q05: How can reinforcement learning frameworks such as ICRL improve tool-use performance in LLM agen

**Answer notes:** Reinforcement learning (RL) frameworks, such as In-Context Reinforcement Learning (ICRL), enable LLMs to learn tool use without expensive supervised fine-tuning . The process involves: Frameworks such as ToolWeaver address these limitations by encoding tools into hierarchical sequences, enabling logarithmic vocabulary expansion and improved learning of collaborative tool relationships .

**Assessment:** definitions, a concrete example, trade-offs and limits.

