# main.py
"""
Hierarchical Orchestrator Prototype
- dispatch(task, profiles):
    * task: dict with at least 'domain' and 'payload' keys
    * profiles: dict mapping domain names to subagent dicts, each with:
        - 'handler': callable(task) -> result dict
        - 'delegates': list of domain names this domain can delegate to
- No cyclic delegation allowed (direct or indirect)
- Returns structured outcome: {'domain': ..., 'result': ..., 'delegated': {...}}
"""
from typing import Any, Dict, Set

def dispatch(task: dict, profiles: dict) -> dict:
    """
    Dispatches a task to the appropriate domain subagent, recursively handling delegation.
    Prevents cyclic delegation.
    """
    if not isinstance(task, dict):
        raise TypeError("task must be a dict")
    if not isinstance(profiles, dict):
        raise TypeError("profiles must be a dict")
    if 'domain' not in task:
        raise ValueError("task must have a 'domain' key")
    if 'payload' not in task:
        raise ValueError("task must have a 'payload' key")
    
    def _dispatch(domain: str, task: dict, profiles: dict, visited: Set[str]) -> dict:
        if domain in visited:
            raise RuntimeError(f"Cyclic delegation detected at domain '{domain}'")
        if domain not in profiles:
            raise ValueError(f"Domain '{domain}' not found in profiles")
        visited = visited | {domain}  # create new set for recursion
        profile = profiles[domain]
        handler = profile.get('handler')
        delegates = profile.get('delegates', [])
        if not callable(handler):
            raise ValueError(f"Handler for domain '{domain}' must be callable")
        # Handler may return a result or a delegation request
        result = handler(task)
        # If handler returns a dict with 'delegate_to', delegate
        if isinstance(result, dict) and 'delegate_to' in result:
            delegate_domain = result['delegate_to']
            if delegate_domain not in delegates:
                raise PermissionError(f"Domain '{domain}' not allowed to delegate to '{delegate_domain}'")
            # Delegate the task (could modify task if needed)
            delegated_result = _dispatch(delegate_domain, task, profiles, visited)
            return {
                'domain': domain,
                'result': None,
                'delegated': delegated_result
            }
        else:
            return {
                'domain': domain,
                'result': result,
                'delegated': None
            }
    return _dispatch(task['domain'], task, profiles, set())

