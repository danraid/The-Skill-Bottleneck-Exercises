# test_lab.py
import unittest
from main import route

class TestSemanticSkillRouter(unittest.TestCase):
    def test_basic_similarity(self):
        query = "Python developer"
        skills = [
            "Senior Python developer",
            "Java developer",
            "Python engineer",
            "C++ developer"
        ]
        # Only Python domain skills: Senior Python developer, Python engineer
        # Senior Python developer shares 2/3 words with query (jaccard=2/3)
        # Python engineer shares 1/3 (jaccard=1/3)
        result = route(query, skills, 2)
        self.assertEqual(result, [
            "Senior Python developer",
            "Python engineer"
        ])

    def test_domain_constraint(self):
        query = "Java developer"
        skills = [
            "Python developer",
            "Java developer",
            "Java architect",
            "C++ developer"
        ]
        # Only Java domain skills
        result = route(query, skills, 3)
        self.assertEqual(result, [
            "Java developer",
            "Java architect"
        ])

    def test_empty_inputs(self):
        self.assertEqual(route("", [], 5), [])
        self.assertEqual(route("", [""], 1), [""])
        self.assertEqual(route("Python", [], 1), [])

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            route(123, ["a"], 1)
        with self.assertRaises(TypeError):
            route("a", "notalist", 1)
        with self.assertRaises(TypeError):
            route("a", [1,2,3], 1)
        with self.assertRaises(TypeError):
            route("a", ["a"], "notanint")

    def test_k_greater_than_skills(self):
        query = "Python developer"
        skills = ["Python developer", "Python engineer"]
        result = route(query, skills, 10)
        self.assertEqual(result, ["Python developer", "Python engineer"])

    def test_k_zero_or_negative(self):
        query = "Python developer"
        skills = ["Python developer", "Python engineer"]
        self.assertEqual(route(query, skills, 0), [])
        self.assertEqual(route(query, skills, -5), [])

    def test_tie_breaking_stability(self):
        query = "Python coder"
        skills = [
            "Python engineer",  # jaccard=1/3
            "Python architect", # jaccard=1/3
            "Python coder"      # jaccard=1.0
        ]
        # coder is best, then engineer and architect tie, but order preserved
        result = route(query, skills, 3)
        self.assertEqual(result, [
            "Python coder",
            "Python engineer",
            "Python architect"
        ])




