# main.py
"""
Deterministic Educational Prototype: Progressive Skill Loading
- Exposes two functions: metadata() and load_selected(skill_id)
- metadata() returns a list of skills with id, name, and summary only
- load_selected(skill_id) returns full instructions for the selected skill only
- No skill's full instructions are revealed unless explicitly selected
"""

from typing import List, Dict, Any, Optional

# Internal skill data (would be in a DB in production)
_SKILLS = [
    {
        "id": "s1",
        "name": "Python Basics",
        "summary": "Learn variables, types, and basic operations.",
        "instructions": "1. Understand variables. 2. Learn data types. 3. Practice arithmetic and string operations."
    },
    {
        "id": "s2",
        "name": "Control Flow",
        "summary": "Master if-statements and loops.",
        "instructions": "1. Write if-else blocks. 2. Use for and while loops. 3. Combine conditions."
    },
    {
        "id": "s3",
        "name": "Functions",
        "summary": "Define and use functions.",
        "instructions": "1. Define functions with def. 2. Pass arguments. 3. Return values. 4. Use docstrings."
    },
]

def metadata() -> List[Dict[str, str]]:
    """
    Returns a list of skills with id, name, and summary only.
    """
    return [
        {"id": s["id"], "name": s["name"], "summary": s["summary"]}
        for s in _SKILLS
    ]

def load_selected(skill_id: str) -> Optional[Dict[str, Any]]:
    """
    Given a skill_id, returns the full skill data (including instructions).
    If not found, returns None.
    """
    for s in _SKILLS:
        if s["id"] == skill_id:
            # Return all fields
            return dict(s)
    return None

