"""Deterministic educational playbook executor.

Failure transitions are validated as a directed graph BEFORE any actions run.
A cycle is invalid even if the corresponding failure branch is not reached.
"""
from typing import Any, Callable

class PlaybookExecutionError(Exception):
    pass

class PlaybookCycleError(PlaybookExecutionError):
    pass

def run_playbook(playbook: list[dict[str, Any]], tools: dict[str, Callable]) -> dict:
    if not isinstance(playbook, list) or not isinstance(tools, dict):
        raise TypeError("Invalid playbook/tools")
    lookup = {}
    for step in playbook:
        if not isinstance(step, dict):
            raise TypeError("Step must be a mapping")
        identifier = step.get("id")
        if not identifier or identifier in lookup:
            raise ValueError("Duplicate or missing step id")
        lookup[identifier] = step
    active, finished = set(), set()
    def validate(node):
        if node in active:
            raise PlaybookCycleError("Failure transition cycle at "+node)
        if node in finished:
            return
        active.add(node)
        next_id = lookup[node].get("on_failure")
        if next_id is not None:
            if next_id not in lookup:
                raise ValueError("Unknown on_failure target: "+str(next_id))
            validate(next_id)
        active.remove(node)
        finished.add(node)
    for key in lookup:
        validate(key)

    states: dict[str,str] = {}
    first_failure = None
    def execute(key):
        nonlocal first_failure
        if key in states:
            return
        step = lookup[key]
        tries = step.get("retries",0)
        if not isinstance(tries,int) or isinstance(tries,bool) or tries<0 or tries>10:
            raise ValueError("Retry count out of bounds")
        passed = False
        for _ in range(tries+1):
            try:
                action = tools.get(step.get("action"))
                if action is None:
                    raise PlaybookExecutionError("Unknown tool")
                result = action(**step.get("args",{}))
                if result is False:
                    continue
                if all(tools[c["action"]](**c.get("args",{}))
                       for c in step.get("checks",[])):
                    passed=True
                    break
            except Exception:
                continue
        states[key] = "success" if passed else "failed"
        if not passed:
            if first_failure is None:
                first_failure=key
            target=step.get("on_failure")
            if target is not None:
                execute(target)
    for key in lookup:
        execute(key)
    return {"steps":states,"failed_step":first_failure}

