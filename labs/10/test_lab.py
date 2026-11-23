# test_lab.py
import unittest
from main import ContextStore

class TestContextStore(unittest.TestCase):
    def setUp(self):
        self.store = ContextStore()
        self.tenant1 = 'tenantA'
        self.tenant2 = 'tenantB'
        self.agent1 = 'agent1'
        self.agent2 = 'agent2'

    def test_isolation_between_agents(self):
        self.store.set(self.tenant1, self.agent1, 'foo', 123)
        self.assertIsNone(self.store.get(self.tenant1, self.agent2, 'foo'))
        self.assertEqual(self.store.get(self.tenant1, self.agent1, 'foo'), 123)

    def test_isolation_between_tenants(self):
        self.store.set(self.tenant1, self.agent1, 'bar', 'abc')
        self.store.set(self.tenant2, self.agent1, 'bar', 'xyz')
        self.assertEqual(self.store.get(self.tenant1, self.agent1, 'bar'), 'abc')
        self.assertEqual(self.store.get(self.tenant2, self.agent1, 'bar'), 'xyz')

    def test_delete_and_clear(self):
        self.store.set(self.tenant1, self.agent1, 'k', 1)
        self.store.set(self.tenant1, self.agent1, 'j', 2)
        self.store.delete(self.tenant1, self.agent1, 'k')
        self.assertIsNone(self.store.get(self.tenant1, self.agent1, 'k'))
        self.assertEqual(self.store.get(self.tenant1, self.agent1, 'j'), 2)
        self.store.clear_agent(self.tenant1, self.agent1)
        self.assertIsNone(self.store.get(self.tenant1, self.agent1, 'j'))

    def test_cross_tenant_agent_access_denied(self):
        self.store.set(self.tenant1, self.agent1, 'secret', 'val')
        # Should not see from other tenant or agent
        self.assertIsNone(self.store.get(self.tenant2, self.agent1, 'secret'))
        self.assertIsNone(self.store.get(self.tenant1, self.agent2, 'secret'))
        self.assertIsNone(self.store.get(self.tenant2, self.agent2, 'secret'))

    def test_list_keys_and_clear_tenant(self):
        self.store.set(self.tenant1, self.agent1, 'a', 1)
        self.store.set(self.tenant1, self.agent1, 'b', 2)
        self.store.set(self.tenant1, self.agent2, 'c', 3)
        keys = self.store.list_keys(self.tenant1, self.agent1)
        self.assertCountEqual(keys, ['a', 'b'])
        self.store.clear_tenant(self.tenant1)
        self.assertEqual(self.store.list_keys(self.tenant1, self.agent1), [])
        self.assertEqual(self.store.list_keys(self.tenant1, self.agent2), [])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            self.store.set('', self.agent1, 'x', 1)
        with self.assertRaises(ValueError):
            self.store.get(self.tenant1, '', 'x')
        with self.assertRaises(ValueError):
            self.store.delete(self.tenant1, self.agent1, '')
        with self.assertRaises(ValueError):
            self.store.clear_agent('', self.agent1)
        with self.assertRaises(ValueError):
            self.store.clear_tenant('')
        with self.assertRaises(ValueError):
            self.store.list_keys(self.tenant1, '')

