# main.py
"""
Skill Registry (Educational Prototype)
Implements a deterministic, versioned skill registry with metadata-only discovery and duplicate prevention.
"""
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict

@dataclass(frozen=True)
class Skill:
    id: str  # Unique identifier for the skill
    version: str  # Version string, e.g., '1.0.0'
    name: str  # Human-readable name
    description: str  # Short description
    author: str  # Author name or contact
    # Additional metadata fields can be added here

    def metadata(self) -> Dict[str, str]:
        """Return metadata-only view (no code, no secrets)."""
        return {
            'id': self.id,
            'version': self.version,
            'name': self.name,
            'description': self.description,
            'author': self.author
        }

class Registry:
    def __init__(self):
        # Key: (id, version), Value: Skill
        self._skills: Dict[tuple, Skill] = {}

    def register(self, skill: Skill) -> bool:
        """
        Register a new skill. Rejects duplicate (id, version) pairs.
        Returns True if successful, False if duplicate.
        """
        key = (skill.id, skill.version)
        if key in self._skills:
            return False
        self._skills[key] = skill
        return True

    def discover(self) -> List[Dict[str, str]]:
        """
        Return a list of metadata-only views for all registered skills.
        """
        return [s.metadata() for s in self._skills.values()]

    def lookup(self, id: str, version: Optional[str] = None) -> Optional[Dict[str, str]]:
        """
        Deterministically lookup a skill by id and (optionally) version.
        Returns metadata-only view or None if not found.
        If version is None, returns the lexicographically highest version for the id.
        """
        candidates = [s for (sid, ver), s in self._skills.items() if sid == id]
        if not candidates:
            return None
        if version is not None:
            for s in candidates:
                if s.version == version:
                    return s.metadata()
            return None
        # No version specified: pick highest lexicographically
        highest = max(candidates, key=lambda s: s.version)
        return highest.metadata()

