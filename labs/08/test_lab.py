# test_lab.py
import unittest
from main import MCPTool, MCPAllowlist, authorised_call, SchemaValidationError, ToolNotAllowedError, ADD_TOOL, GREET_TOOL

class TestMCPIntegrationLayer(unittest.TestCase):
    def setUp(self):
        self.allowlist = MCPAllowlist(['add', 'greet'])
        self.denylist = MCPAllowlist([])

    def test_successful_add(self):
        result = authorised_call(ADD_TOOL, {'x': 2, 'y': 3}, self.allowlist)
        self.assertEqual(result, 5)

    def test_schema_mismatch_type(self):
        # y should be int, not str
        with self.assertRaises(SchemaValidationError):
            authorised_call(ADD_TOOL, {'x': 2, 'y': 'oops'}, self.allowlist)

    def test_schema_missing_param(self):
        # Missing 'y'
        with self.assertRaises(SchemaValidationError):
            authorised_call(ADD_TOOL, {'x': 2}, self.allowlist)

    def test_schema_extra_param(self):
        # Extra param 'z'
        with self.assertRaises(SchemaValidationError):
            authorised_call(ADD_TOOL, {'x': 2, 'y': 3, 'z': 99}, self.allowlist)

    def test_tool_not_allowed(self):
        # 'add' not in denylist
        with self.assertRaises(ToolNotAllowedError):
            authorised_call(ADD_TOOL, {'x': 1, 'y': 2}, self.denylist)

    def test_greet_tool(self):
        result = authorised_call(GREET_TOOL, {'name': 'Alice'}, self.allowlist)
        self.assertEqual(result, 'Hello, Alice!')

    def test_greet_tool_wrong_type(self):
        with self.assertRaises(SchemaValidationError):
            authorised_call(GREET_TOOL, {'name': 123}, self.allowlist)

    def test_greet_tool_not_allowed(self):
        with self.assertRaises(ToolNotAllowedError):
            authorised_call(GREET_TOOL, {'name': 'Bob'}, self.denylist)

if __name__ == '__main__':
    unittest.main()

