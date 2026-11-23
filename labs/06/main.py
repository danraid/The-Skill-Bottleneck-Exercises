# main.py
from typing import FrozenSet, Set, Optional
from dataclasses import dataclass, field

# Allowed tools for subagents
_ALLOWED_TOOLS = frozenset({
    'search',
    'summarize',
    'translate',
    'calculate',
    'extract',
})

@dataclass(frozen=True)
class SubagentProfile:
    name: str
    role: str
    tools: FrozenSet[str] = field(default_factory=frozenset)

    def has_tool(self, tool: str) -> bool:
        return tool in self.tools

    def describe(self) -> str:
        return f"Subagent '{self.name}' ({self.role}) with tools: {sorted(self.tools)}"

def create_subagent_profile(name: str, role: str, tools: Optional[Set[str]] = None) -> SubagentProfile:
    """
    Factory function to create an immutable SubagentProfile.
    Only allows permitted tools. Denies unauthorized tools.
    Each instance is isolated (no shared mutable state).
    """
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Subagent name must be a non-empty string.")
    if not isinstance(role, str) or not role.strip():
        raise ValueError("Subagent role must be a non-empty string.")
    if tools is None:
        tools = set()
    if not isinstance(tools, (set, frozenset)):
        raise TypeError("tools must be a set or frozenset of strings.")
    unauthorized = set(tools) - _ALLOWED_TOOLS
    if unauthorized:
        raise PermissionError(f"Unauthorized tools requested: {sorted(unauthorized)}")
    return SubagentProfile(name=name.strip(), role=role.strip(), tools=frozenset(tools))

