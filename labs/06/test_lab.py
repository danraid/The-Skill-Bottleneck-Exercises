# test_lab.py
import unittest
from main import create_subagent_profile, SubagentProfile

class TestSubagentProfileFactory(unittest.TestCase):
    def test_valid_profile_creation(self):
        profile = create_subagent_profile(
            name="Alice",
            role="Researcher",
            tools={"search", "summarize"}
        )
        self.assertIsInstance(profile, SubagentProfile)
        self.assertEqual(profile.name, "Alice")
        self.assertEqual(profile.role, "Researcher")
        self.assertEqual(profile.tools, frozenset({"search", "summarize"}))
        self.assertTrue(profile.has_tool("search"))
        self.assertFalse(profile.has_tool("translate"))

    def test_unauthorized_tool_denied(self):
        with self.assertRaises(PermissionError) as cm:
            create_subagent_profile(
                name="Bob",
                role="Analyst",
                tools={"search", "hack"}
            )
        self.assertIn("Unauthorized tools requested", str(cm.exception))
        self.assertIn("hack", str(cm.exception))

    def test_profile_is_immutable(self):
        profile = create_subagent_profile(
            name="Carol",
            role="Translator",
            tools={"translate"}
        )
        with self.assertRaises(Exception):
            profile.name = "Eve"
        with self.assertRaises(Exception):
            profile.tools.add("search")

    def test_isolation_between_instances(self):
        profile1 = create_subagent_profile(
            name="Dave",
            role="Calculator",
            tools={"calculate"}
        )
        profile2 = create_subagent_profile(
            name="Eve",
            role="Extractor",
            tools={"extract"}
        )
        self.assertNotEqual(profile1, profile2)
        self.assertNotEqual(profile1.tools, profile2.tools)
        # Changing one does not affect the other (immutability)
        self.assertTrue(profile1.has_tool("calculate"))
        self.assertFalse(profile2.has_tool("calculate"))

    def test_empty_tools_allowed(self):
        profile = create_subagent_profile(
            name="Frank",
            role="Observer",
            tools=set()
        )
        self.assertEqual(profile.tools, frozenset())
        self.assertFalse(profile.has_tool("search"))

    def test_invalid_name_or_role(self):
        with self.assertRaises(ValueError):
            create_subagent_profile(name="", role="Agent", tools={"search"})
        with self.assertRaises(ValueError):
            create_subagent_profile(name="Agent007", role="", tools={"search"})
        with self.assertRaises(ValueError):
            create_subagent_profile(name="   ", role="Spy", tools={"search"})
        with self.assertRaises(ValueError):
            create_subagent_profile(name="Spy", role="   ", tools={"search"})

    def test_tools_type_enforcement(self):
        with self.assertRaises(TypeError):
            create_subagent_profile(name="Gina", role="Analyst", tools=["search"])  # list, not set
        with self.assertRaises(TypeError):
            create_subagent_profile(name="Hank", role="Analyst", tools="search")  # str, not set

