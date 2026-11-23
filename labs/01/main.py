# main.py
"""
Monolithic Agent Skill Selector (Educational Prototype)
Implements select_skill(task, skills) per specification 01.
- Deterministically selects a skill from a catalogue matching the task.
- Logs selected skill id to an internal log (accessible via get_log()).
- Handles missing capabilities.
- No external dependencies; pure Python 3.12 stdlib.
"""
from typing import Any, Dict, List, Optional

# Internal log for demonstration (not persistent, not file-based)
_log: List[str] = []

def get_log() -> List[str]:
    """Return a copy of the internal log."""
    return list(_log)

def clear_log() -> None:
    """Clear the internal log (for testing)."""
    _log.clear()

def select_skill(task: Dict[str, Any], skills: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
    """
    Select a valid skill from skills that can handle the task.
    - task: dict with at least 'requirements': List[str]
    - skills: list of dicts, each with at least 'id' (str) and 'capabilities': List[str]
    Returns the selected skill dict, or None if no skill matches.
    Logs the selected skill id if selection is made.
    Deterministic: selects the first matching skill in skills list.
    """
    requirements = task.get('requirements', [])
    if not isinstance(requirements, list):
        raise ValueError("Task 'requirements' must be a list.")
    for skill in skills:
        capabilities = skill.get('capabilities', [])
        if not isinstance(capabilities, list):
            continue  # skip malformed skill
        if all(req in capabilities for req in requirements):
            skill_id = str(skill.get('id', 'unknown'))
            _log.append(f"Selected skill id: {skill_id}")
            return skill
    # No matching skill found
    _log.append("No valid skill found for task.")
    return None

