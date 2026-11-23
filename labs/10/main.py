# main.py
"""
Context Isolation Manager (ContextStore)
Deterministic educational prototype.
"""
from typing import Any, Dict, Optional
import threading

class ContextStore:
    """
    ContextStore safely scopes agent state per (tenant_id, agent_id).
    No cross-agent or cross-tenant disclosure.
    Thread-safe for educational purposes.
    """
    def __init__(self):
        # _store: Dict[tenant_id, Dict[agent_id, Dict[str, Any]]]
        self._store: Dict[str, Dict[str, Dict[str, Any]]] = {}
        self._lock = threading.Lock()

    def set(self, tenant_id: str, agent_id: str, key: str, value: Any) -> None:
        """Set a value for a key scoped to (tenant_id, agent_id)."""
        if not tenant_id or not agent_id or not key:
            raise ValueError("tenant_id, agent_id, and key must be non-empty strings")
        with self._lock:
            self._store.setdefault(tenant_id, {})
            self._store[tenant_id].setdefault(agent_id, {})
            self._store[tenant_id][agent_id][key] = value

    def get(self, tenant_id: str, agent_id: str, key: str) -> Optional[Any]:
        """Get a value for a key scoped to (tenant_id, agent_id). Returns None if not found."""
        if not tenant_id or not agent_id or not key:
            raise ValueError("tenant_id, agent_id, and key must be non-empty strings")
        with self._lock:
            return self._store.get(tenant_id, {}).get(agent_id, {}).get(key)

    def delete(self, tenant_id: str, agent_id: str, key: str) -> None:
        """Delete a key for (tenant_id, agent_id)."""
        if not tenant_id or not agent_id or not key:
            raise ValueError("tenant_id, agent_id, and key must be non-empty strings")
        with self._lock:
            agent_ctx = self._store.get(tenant_id, {}).get(agent_id)
            if agent_ctx and key in agent_ctx:
                del agent_ctx[key]

    def clear_agent(self, tenant_id: str, agent_id: str) -> None:
        """Remove all keys for a given agent in a tenant."""
        if not tenant_id or not agent_id:
            raise ValueError("tenant_id and agent_id must be non-empty strings")
        with self._lock:
            if tenant_id in self._store and agent_id in self._store[tenant_id]:
                del self._store[tenant_id][agent_id]
                if not self._store[tenant_id]:
                    del self._store[tenant_id]

    def clear_tenant(self, tenant_id: str) -> None:
        """Remove all agents and keys for a tenant."""
        if not tenant_id:
            raise ValueError("tenant_id must be a non-empty string")
        with self._lock:
            if tenant_id in self._store:
                del self._store[tenant_id]

    def list_keys(self, tenant_id: str, agent_id: str) -> list[str]:
        """List all keys for a given (tenant_id, agent_id)."""
        if not tenant_id or not agent_id:
            raise ValueError("tenant_id and agent_id must be non-empty strings")
        with self._lock:
            return list(self._store.get(tenant_id, {}).get(agent_id, {}).keys())

