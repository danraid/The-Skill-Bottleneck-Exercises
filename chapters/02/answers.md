# Chapter 02: Worked Answers

The reference responses are based on the corresponding chapter. Open-ended assignments can admit multiple correct designs.

## Exercise solutions

### E01: Tool Registry Expansion: Add at least two new tools to the registry, including their descriptio

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations 1. Compute semantic similarity between the query and each tool’s description. 2. Retrieve trust scores for each tool. 3. Combine similarity and trust into a composite score. 4. Rank tools and select the highest-scoring candidate.

**Reference code:** [Lab 02](../../labs/02/README.md).

### E02: Trust Score Dynamics: Simulate a scenario where a tool’s trust score drops due to repeated fail

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations 1. Intent Interpretation: Parsing and understanding the user’s request or the agent’s current goal. 2. Goal Decomposition: Breaking down complex tasks into manageable sub-tasks or steps. 3. Tool Discovery and Selection: - Tool Registry Query: Searching the registry for candidate tools based on semantic matching and metadata . - Trust and Capability Assessment: Evaluating tools for reliability, availability, and suitability . 4

**Reference code:** [Lab 02](../../labs/02/README.md).

### E03: Adversarial Tool Injection: Add a tool with a misleading description. Observe how the agent ski

**Reference approach:** Define trusted versus untrusted inputs, a tool allowlist and an explicit unauthorized-call denial case; record a structured audit trace.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** Agent skills are vulnerable to prompt injection and adversarial tool definitions. For example, malicious tool documents can manipulate tool selection, compelling the agent to choose attacker-controlled tools . Existing defences (e.g., structure-based or perplexity-based detection) are not fully effective, highlighting the need for robust security strategies. - Context Window Saturation: As the number of tools and the complexity of tasks grow, LLMs may struggle to encode all relevant tool metadata within their context window, limiting discoverability and selection accuracy . - Security Vulnerabilities: Prompt injection and adversarial tool definitions remain unsolved problems, with current defences offering only partial protection . - Interpretability Gaps: While mechanistic interp

**Reference code:** [Lab 02](../../labs/02/README.md).

### E04: Context Handling: Modify the agent to handle multi-step queries (e.g., “Calculate the sum of to

**Reference approach:** Separate discovery metadata from detailed tool instructions, measure context exposed, and test retrieval and information-isolation edge cases.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations - Define what constitutes an agent skill in the context of agentic AI and distinguish it from basic tool invocation. - Describe the architectural components and workflow of agent skills, including reasoning, tool selection, execution, and monitoring. - Explain the trade-offs and challenges associated with agent skill design, such as scalability, reliability, and security. - Implement a basic agent skill in Python, demonstratin

**Reference code:** [Lab 02](../../labs/02/README.md).

### E05: Interpretability: Implement simple logging to explain why a particular tool was selected for a 

**Reference approach:** Implement the proposed capability through an explicit interface, a reproducible test fixture and at least one normal and one failure case; state architectural trade-offs.

**Acceptance tests:** normal behaviour, invalid inputs, authorization where applicable, observable traces, and stated limitations.

**Chapter evidence:** Extend the orchestration to handle errors and allow user feedback for trust score adjustment. Implement logging to record decision points for interpretability. Design and implement a basic agent skill that interprets a user query, selects a tool from a registry based on semantic similarity and trust score, invokes the tool, and returns the result. Extend the implementation to support error handling, logging for interpretability, and feedback-driven trust adjustment.

**Reference code:** [Lab 02](../../labs/02/README.md).

## Review-question answers

### Q01: What are the essential components of an agent skill, and how do they interact?

**Answer notes:** This chapter systematically dissects the anatomy of an agent skill, grounding each component in current research and best practices. We explore how agent skills are structured, how they interact with external tools, and how they are orchestrated within modern agentic AI frameworks. Advanced topics such as trust-aware tool selection, interpretability, security, and the challenges of long-context reasoning are also addressed, pr - Define what constitutes an agent skill in the context of agentic AI and distinguish it from basic tool invocation. - Describe the architectural components and workflow of agent skills, including reasoning, tool selection, execution, and monitoring. - Explain the trade-offs and challenges associated with agent skill design, such as scalability, reliability, and security. - Implement a basic agent skill in Python, demonstratin

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q02: How does dynamic tool selection differ from static tool invocation?

**Answer notes:** - Define what constitutes an agent skill in the context of agentic AI and distinguish it from basic tool invocation. - Describe the architectural components and workflow of agent skills, including reasoning, tool selection, execution, and monitoring. - Explain the trade-offs and challenges associated with agent skill design, such as scalability, reliability, and security. - Implement a basic agent skill in Python, demonstratin - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q03: What role does the tool registry play in agent skill orchestration?

**Answer notes:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations 1. Intent Interpretation: Parsing and understanding the user’s request or the agent’s current goal. 2. Goal Decomposition: Breaking down complex tasks into manageable sub-tasks or steps. 3. Tool Discovery and Selection: - Tool Registry Query: Searching the registry for candidate tools based on semantic matching and metadata . - Trust and Capability Assessment: Evaluating tools for reliability, availability, and suitability . 4

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q04: Why is trust scoring important in tool selection, and what signals can be used?

**Answer notes:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations - Task Interpretation: Understanding the user’s intent and decomposing it into actionable steps. - Dynamic Tool Selection: Choosing the best tool based on task requirements, tool capabilities, and runtime trust signals . - Execution and Monitoring: Invoking the tool, monitoring execution, and handling errors or exceptions. - Feedback Integration: Adapting future actions based on outcomes, user feedback, or environmental change

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q05: What are the main security risks associated with agent skills, and what defences have been prop

**Answer notes:** - Define what constitutes an agent skill in the context of agentic AI and distinguish it from basic tool invocation. - Describe the architectural components and workflow of agent skills, including reasoning, tool selection, execution, and monitoring. - Explain the trade-offs and challenges associated with agent skill design, such as scalability, reliability, and security. - Implement a basic agent skill in Python, demonstratin Agent skills are vulnerable to prompt injection and adversarial tool definitions. For example, malicious tool documents can manipulate tool selection, compelling the agent to choose attacker-controlled tools . Existing defences (e.g., structure-based or perplexity-based detection) are not fully effective, highlighting the need for robust security strategies.

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q06: How does the “lost-in-the-middle” effect impact agent skill performance in long-context scenari

**Answer notes:** - Agentic AI: AI systems exhibiting autonomy, proactivity, and adaptive workflow control, often through dynamic tool selection and multi-step reasoning . - Agent Skill: A modular capability or workflow step that an agent can invoke, encompassing task interpretation, tool selection, execution, and monitoring . - Tool: An external software component or API that performs a specific function, such as database queries, calculations Long-context reasoning introduces challenges such as the "lost-in-the-middle" effect, where information in the middle of a long context is less reliably retrieved . The difficulty of reasoning is not solely a function of context length but also of evidence scope, dispersion, and reasoning depth .

**Assessment:** definitions, a concrete example, trade-offs and limits.

### Q07: In what ways can agent skills be made more interpretable and auditable? ---

**Answer notes:** The Model Context Protocol (MCP) provides a standardised interface for tool registration and invocation, enabling scalable tool selection in multi-server environments . Recent studies show that even minimal metadata (such as qualified tool names) can suffice for effective tool routing, especially for smaller models, while richer descriptions become more valuable as model size increases.

**Assessment:** definitions, a concrete example, trade-offs and limits.

