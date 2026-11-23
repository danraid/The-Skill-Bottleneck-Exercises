# test_lab.py
import unittest
from main import select_skill, get_log, clear_log

class TestSelectSkill(unittest.TestCase):
    def setUp(self):
        clear_log()

    def test_selects_first_matching_skill(self):
        skills = [
            {'id': 's1', 'capabilities': ['read', 'write']},
            {'id': 's2', 'capabilities': ['read', 'execute']},
        ]
        task = {'requirements': ['read']}
        selected = select_skill(task, skills)
        self.assertIsNotNone(selected)
        self.assertEqual(selected['id'], 's1')
        self.assertIn('Selected skill id: s1', get_log()[-1])

    def test_no_skill_matches(self):
        skills = [
            {'id': 's1', 'capabilities': ['read']},
            {'id': 's2', 'capabilities': ['write']},
        ]
        task = {'requirements': ['execute']}
        selected = select_skill(task, skills)
        self.assertIsNone(selected)
        self.assertIn('No valid skill found for task.', get_log()[-1])

    def test_empty_skills_list(self):
        skills = []
        task = {'requirements': ['read']}
        selected = select_skill(task, skills)
        self.assertIsNone(selected)
        self.assertIn('No valid skill found for task.', get_log()[-1])

    def test_skill_with_missing_capabilities_field(self):
        skills = [
            {'id': 's1'},  # No 'capabilities' key
            {'id': 's2', 'capabilities': ['read', 'write']},
        ]
        task = {'requirements': ['write']}
        selected = select_skill(task, skills)
        self.assertIsNotNone(selected)
        self.assertEqual(selected['id'], 's2')
        self.assertIn('Selected skill id: s2', get_log()[-1])

    def test_task_with_non_list_requirements_raises(self):
        skills = [{'id': 's1', 'capabilities': ['read']}]
        task = {'requirements': 'read'}  # Not a list
        with self.assertRaises(ValueError):
            select_skill(task, skills)

    def test_skill_with_non_list_capabilities_skipped(self):
        skills = [
            {'id': 's1', 'capabilities': 'read'},  # Not a list
            {'id': 's2', 'capabilities': ['read']},
        ]
        task = {'requirements': ['read']}
        selected = select_skill(task, skills)
        self.assertIsNotNone(selected)
        self.assertEqual(selected['id'], 's2')

if __name__ == '__main__':
    unittest.main()

