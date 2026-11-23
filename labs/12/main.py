# main.py
"""
Deterministic educational prototype for Skill Scalability Benchmark
Implements: evaluate(registry, tasks, adapters)
"""
from typing import Any, Dict, List, Callable, Tuple
import copy
import random


def evaluate(registry: Dict[str, Callable], tasks: List[Dict[str, Any]], adapters: Dict[str, Callable]) -> Dict[str, Any]:
    """
    Evaluate adapters on a fixed suite of tasks using registered functions.
    Separates proxy (adapter) outcomes from real (registry) outcomes.
    Ensures reproducibility by protecting the split (no randomization unless seeded).
    No fabricated empirical claims; only deterministic, reproducible results.

    Args:
        registry: Dict mapping task names to reference callable implementations.
        tasks: List of dicts, each describing a task with at least a 'name' field.
        adapters: Dict mapping adapter names to callable implementations.

    Returns:
        Dict with keys:
            'proxy': {adapter: {task: result}}
            'real': {task: result}
            'tasks': [task names]
            'adapters': [adapter names]
    """
    # Defensive copy to avoid mutation
    tasks = copy.deepcopy(tasks)
    # Sort tasks and adapters for reproducibility
    task_names = [t['name'] for t in tasks]
    adapters_sorted = sorted(adapters.keys())
    results = {
        'proxy': {},
        'real': {},
        'tasks': task_names,
        'adapters': adapters_sorted
    }
    # Evaluate real outcomes
    for task in tasks:
        name = task['name']
        func = registry.get(name)
        if func is None:
            results['real'][name] = {'error': 'Task not in registry'}
        else:
            try:
                results['real'][name] = {'result': func(**task.get('input', {}))}
            except Exception as e:
                results['real'][name] = {'error': str(e)}
    # Evaluate proxy (adapter) outcomes
    for adapter_name in adapters_sorted:
        adapter_func = adapters[adapter_name]
        results['proxy'][adapter_name] = {}
        for task in tasks:
            name = task['name']
            try:
                results['proxy'][adapter_name][name] = {'result': adapter_func(name, task.get('input', {}))}
            except Exception as e:
                results['proxy'][adapter_name][name] = {'error': str(e)}
    return results

