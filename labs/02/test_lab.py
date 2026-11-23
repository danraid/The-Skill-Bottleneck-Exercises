# test_lab.py
import unittest
from main import Skill, Registry

class TestSkillRegistry(unittest.TestCase):
    def setUp(self):
        self.registry = Registry()
        self.skill1 = Skill(
            id="nlp.tokenize",
            version="1.0.0",
            name="Tokenizer",
            description="Splits text into tokens.",
            author="Alice"
        )
        self.skill2 = Skill(
            id="nlp.tokenize",
            version="1.1.0",
            name="Tokenizer",
            description="Splits text into tokens (improved).",
            author="Alice"
        )
        self.skill3 = Skill(
            id="vision.detect",
            version="2.0.0",
            name="Object Detector",
            description="Detects objects in images.",
            author="Bob"
        )

    def test_register_and_discover(self):
        self.assertTrue(self.registry.register(self.skill1))
        self.assertTrue(self.registry.register(self.skill3))
        discovered = self.registry.discover()
        self.assertEqual(len(discovered), 2)
        # Metadata-only: must not expose extra fields
        for meta in discovered:
            self.assertIn('id', meta)
            self.assertIn('version', meta)
            self.assertIn('name', meta)
            self.assertIn('description', meta)
            self.assertIn('author', meta)
            self.assertEqual(len(meta), 5)

    def test_duplicate_id_version_rejected(self):
        self.assertTrue(self.registry.register(self.skill1))
        duplicate = Skill(
            id="nlp.tokenize",
            version="1.0.0",
            name="Tokenizer Duplicate",
            description="Should not be allowed.",
            author="Eve"
        )
        self.assertFalse(self.registry.register(duplicate))
        discovered = self.registry.discover()
        self.assertEqual(len(discovered), 1)
        self.assertEqual(discovered[0]['name'], "Tokenizer")

    def test_lookup_deterministic(self):
        self.registry.register(self.skill1)
        self.registry.register(self.skill2)
        # Lookup by id and version
        meta = self.registry.lookup("nlp.tokenize", "1.0.0")
        self.assertIsNotNone(meta)
        self.assertEqual(meta['version'], "1.0.0")
        # Lookup by id only: should get highest version
        meta2 = self.registry.lookup("nlp.tokenize")
        self.assertIsNotNone(meta2)
        self.assertEqual(meta2['version'], "1.1.0")

    def test_lookup_not_found(self):
        self.registry.register(self.skill1)
        # Wrong id
        self.assertIsNone(self.registry.lookup("nonexistent"))
        # Wrong version
        self.assertIsNone(self.registry.lookup("nlp.tokenize", "9.9.9"))

if __name__ == "__main__":
    unittest.main()

