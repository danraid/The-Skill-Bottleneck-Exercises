# main.py
"""
Skill Conflict Detector (Educational Prototype)
Detects overlapping capabilities and incompatible declarative policies among skills.
"""
from typing import List, Dict, Any

def detect_conflicts(skills: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Detects overlapping capabilities and incompatible policies among skills.
    Each skill is a dict with at least:
      - 'id': unique identifier (str or int)
      - 'capabilities': list of capability strings
      - 'policies': dict of policy_name: policy_value
    Returns a list of conflict reports, each with:
      - 'type': 'overlap' or 'policy_conflict'
      - 'skills': list of involved skill IDs
      - 'details': description
    """
    conflicts = []
    n = len(skills)
    # Build lookup for quick access
    id_to_skill = {s['id']: s for s in skills}
    # Overlapping capabilities
    for i in range(n):
        for j in range(i+1, n):
            s1 = skills[i]
            s2 = skills[j]
            set1 = set(s1.get('capabilities', []))
            set2 = set(s2.get('capabilities', []))
            overlap = set1 & set2
            if overlap:
                conflicts.append({
                    'type': 'overlap',
                    'skills': [s1['id'], s2['id']],
                    'details': f"Overlapping capabilities: {sorted(overlap)}"
                })
            # Policy conflicts
            policies1 = s1.get('policies', {})
            policies2 = s2.get('policies', {})
            for key in set(policies1) & set(policies2):
                val1 = policies1[key]
                val2 = policies2[key]
                # Incompatible if values are not equal and not None
                if val1 != val2:
                    conflicts.append({
                        'type': 'policy_conflict',
                        'skills': [s1['id'], s2['id']],
                        'details': f"Policy '{key}' conflict: {val1!r} vs {val2!r}"
                    })
    return conflicts

