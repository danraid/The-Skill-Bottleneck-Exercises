# main.py
"""
Deterministic educational prototype for a Production Agent Platform.
Implements registry, routes, profiles, playbooks, and policy enforcement
with tenant isolation and end-to-end task contract.
"""
from typing import Dict, Any, Callable, Optional
import threading

class PolicyViolation(Exception):
    pass

class NotFound(Exception):
    pass

class PermissionDenied(Exception):
    pass

class Platform:
    def __init__(self):
        # Each tenant has its own isolated registry, routes, profiles, playbooks, and policies
        self._tenants: Dict[str, Dict[str, Any]] = {}
        self._lock = threading.Lock()

    def _get_tenant(self, tenant: str) -> Dict[str, Any]:
        with self._lock:
            if tenant not in self._tenants:
                # Initialize tenant data
                self._tenants[tenant] = {
                    'registry': {},
                    'routes': {},
                    'profiles': {},
                    'playbooks': {},
                    'policies': {},
                }
            return self._tenants[tenant]

    # Registry: Register and retrieve agents
    def register_agent(self, tenant: str, agent_id: str, agent_info: dict):
        t = self._get_tenant(tenant)
        t['registry'][agent_id] = agent_info.copy()

    def get_agent(self, tenant: str, agent_id: str) -> dict:
        t = self._get_tenant(tenant)
        if agent_id not in t['registry']:
            raise NotFound(f"Agent {agent_id} not found for tenant {tenant}")
        return t['registry'][agent_id].copy()

    # Routes: Map tasks to agents
    def add_route(self, tenant: str, task_type: str, agent_id: str):
        t = self._get_tenant(tenant)
        if agent_id not in t['registry']:
            raise NotFound(f"Agent {agent_id} not found for tenant {tenant}")
        t['routes'][task_type] = agent_id

    def get_route(self, tenant: str, task_type: str) -> str:
        t = self._get_tenant(tenant)
        if task_type not in t['routes']:
            raise NotFound(f"No route for task {task_type} for tenant {tenant}")
        return t['routes'][task_type]

    # Profiles: Store agent profiles
    def set_profile(self, tenant: str, agent_id: str, profile: dict):
        t = self._get_tenant(tenant)
        if agent_id not in t['registry']:
            raise NotFound(f"Agent {agent_id} not found for tenant {tenant}")
        t['profiles'][agent_id] = profile.copy()

    def get_profile(self, tenant: str, agent_id: str) -> dict:
        t = self._get_tenant(tenant)
        if agent_id not in t['profiles']:
            raise NotFound(f"Profile for agent {agent_id} not found for tenant {tenant}")
        return t['profiles'][agent_id].copy()

    # Playbooks: Store and run playbooks (task contracts)
    def add_playbook(self, tenant: str, playbook_id: str, playbook: Callable[[dict], dict]):
        t = self._get_tenant(tenant)
        t['playbooks'][playbook_id] = playbook

    def run_playbook(self, tenant: str, playbook_id: str, input_data: dict) -> dict:
        t = self._get_tenant(tenant)
        if playbook_id not in t['playbooks']:
            raise NotFound(f"Playbook {playbook_id} not found for tenant {tenant}")
        # Policy enforcement before running playbook
        self._enforce_policy(tenant, 'run_playbook', playbook_id, input_data)
        playbook = t['playbooks'][playbook_id]
        # Playbook is a deterministic function: dict -> dict
        output = playbook(input_data.copy())
        return output

    # Policy enforcement: Set and check policies
    def set_policy(self, tenant: str, action: str, policy_fn: Callable[[str, Any, Any], bool]):
        t = self._get_tenant(tenant)
        t['policies'][action] = policy_fn

    def _enforce_policy(self, tenant: str, action: str, subject: Any, context: Any):
        t = self._get_tenant(tenant)
        policy_fn = t['policies'].get(action)
        if policy_fn is not None:
            allowed = policy_fn(subject, context, tenant)
            if not allowed:
                raise PermissionDenied(f"Policy denied action {action} for subject {subject} in tenant {tenant}")

    # Tenant isolation: No cross-tenant access
    def cross_tenant_get_agent(self, from_tenant: str, target_tenant: str, agent_id: str):
        if from_tenant != target_tenant:
            raise PermissionDenied("Cross-tenant access denied")
        return self.get_agent(target_tenant, agent_id)

