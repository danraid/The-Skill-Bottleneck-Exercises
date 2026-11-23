# main.py
"""
Deterministic educational prototype: MCP Integration Layer
- Represent tool schemas
- Maintain allowlists
- Enforce client/server call-contract guards (no network)
"""
from typing import Any, Dict, Callable, List

class SchemaValidationError(Exception):
    pass

class ToolNotAllowedError(Exception):
    pass

class MCPTool:
    """
    Represents a tool with a name and a schema (dict of param: type)
    """
    def __init__(self, name: str, schema: Dict[str, type], func: Callable):
        self.name = name
        self.schema = schema  # e.g., {'x': int, 'y': str}
        self.func = func

    def validate(self, params: Dict[str, Any]) -> None:
        # Check all required keys are present and types match
        for key, typ in self.schema.items():
            if key not in params:
                raise SchemaValidationError(f"Missing parameter: {key}")
            if not isinstance(params[key], typ):
                raise SchemaValidationError(f"Parameter '{key}' should be {typ.__name__}, got {type(params[key]).__name__}")
        # No extra keys allowed
        for key in params:
            if key not in self.schema:
                raise SchemaValidationError(f"Unexpected parameter: {key}")

    def call(self, params: Dict[str, Any]) -> Any:
        self.validate(params)
        return self.func(**params)

class MCPAllowlist:
    """
    Maintains a set of allowed tool names
    """
    def __init__(self, allowed_tools: List[str]):
        self.allowed = set(allowed_tools)

    def is_allowed(self, tool_name: str) -> bool:
        return tool_name in self.allowed

def authorised_call(tool: MCPTool, params: Dict[str, Any], allowlist: MCPAllowlist) -> Any:
    """
    Calls the tool if and only if it is allowed and params match schema.
    Raises ToolNotAllowedError or SchemaValidationError as appropriate.
    """
    if not allowlist.is_allowed(tool.name):
        raise ToolNotAllowedError(f"Tool '{tool.name}' is not allowed.")
    return tool.call(params)

# Example tools for demonstration

def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"

ADD_TOOL = MCPTool('add', {'x': int, 'y': int}, add)
GREET_TOOL = MCPTool('greet', {'name': str}, greet)

