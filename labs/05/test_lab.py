# test_lab.py
import unittest
from main import detect_conflicts

class TestSkillConflictDetector(unittest.TestCase):
    def test_no_conflicts(self):
        skills = [
            {'id': 'A', 'capabilities': ['read'], 'policies': {'mode': 'safe'}},
            {'id': 'B', 'capabilities': ['write'], 'policies': {'mode': 'safe'}},
        ]
        result = detect_conflicts(skills)
        self.assertEqual(result, [])

    def test_overlap_conflict(self):
        skills = [
            {'id': 1, 'capabilities': ['read', 'write'], 'policies': {}},
            {'id': 2, 'capabilities': ['write', 'execute'], 'policies': {}},
        ]
        result = detect_conflicts(skills)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['type'], 'overlap')
        self.assertIn('write', result[0]['details'])
        self.assertEqual(set(result[0]['skills']), {1,2})

    def test_policy_conflict(self):
        skills = [
            {'id': 'X', 'capabilities': ['foo'], 'policies': {'level': 'high'}},
            {'id': 'Y', 'capabilities': ['bar'], 'policies': {'level': 'low'}},
        ]
        result = detect_conflicts(skills)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0]['type'], 'policy_conflict')
        self.assertIn("'level' conflict", result[0]['details'])
        self.assertEqual(set(result[0]['skills']), {'X','Y'})

    def test_multiple_conflicts(self):
        skills = [
            {'id': 'A', 'capabilities': ['alpha', 'beta'], 'policies': {'mode': 'safe', 'access': 'full'}},
            {'id': 'B', 'capabilities': ['beta', 'gamma'], 'policies': {'mode': 'unsafe', 'access': 'full'}},
            {'id': 'C', 'capabilities': ['delta'], 'policies': {'mode': 'safe', 'access': 'none'}},
        ]
        result = detect_conflicts(skills)
        # Should detect: overlap A/B (beta), policy_conflict A/B (mode), policy_conflict A/C (access), policy_conflict B/C (access)
        types = [r['type'] for r in result]
        self.assertIn('overlap', types)
        self.assertGreaterEqual(types.count('policy_conflict'), 3)
        # Check traceable IDs
        for r in result:
            self.assertTrue('skills' in r and len(r['skills']) == 2)

    def test_empty_input(self):
        self.assertEqual(detect_conflicts([]), [])

if __name__ == '__main__':
    unittest.main()

