# test_lab.py
import unittest
import main

class TestProgressiveSkillLoading(unittest.TestCase):
    def test_metadata_no_instructions(self):
        meta = main.metadata()
        self.assertIsInstance(meta, list)
        self.assertGreaterEqual(len(meta), 3)
        for skill in meta:
            self.assertIn('id', skill)
            self.assertIn('name', skill)
            self.assertIn('summary', skill)
            self.assertNotIn('instructions', skill)

    def test_load_selected_returns_full_skill(self):
        meta = main.metadata()
        skill_id = meta[0]['id']
        skill = main.load_selected(skill_id)
        self.assertIsInstance(skill, dict)
        self.assertIn('id', skill)
        self.assertIn('name', skill)
        self.assertIn('summary', skill)
        self.assertIn('instructions', skill)
        self.assertEqual(skill['id'], skill_id)

    def test_load_selected_invalid_id(self):
        result = main.load_selected('nonexistent')
        self.assertIsNone(result)

    def test_metadata_does_not_leak_instructions(self):
        # Ensure that instructions are never present in metadata output
        meta = main.metadata()
        for skill in meta:
            for value in skill.values():
                self.assertNotIn('instructions', str(value).lower())

if __name__ == '__main__':
    unittest.main()

