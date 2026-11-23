# test_lab.py
import unittest
from main import Platform, NotFound, PermissionDenied

def dummy_playbook(input_data):
    # Deterministic: returns input incremented by 1 if 'x' in input
    return {'y': input_data.get('x', 0) + 1}

def deny_all(subject, context, tenant):
    return False

def allow_all(subject, context, tenant):
    return True

class TestPlatform(unittest.TestCase):
    def setUp(self):
        self.platform = Platform()
        self.tenant = 'tenantA'
        self.agent_id = 'agent1'
        self.agent_info = {'name': 'Agent One', 'role': 'worker'}

    def test_register_and_get_agent(self):
        self.platform.register_agent(self.tenant, self.agent_id, self.agent_info)
        agent = self.platform.get_agent(self.tenant, self.agent_id)
        self.assertEqual(agent, self.agent_info)

    def test_route_and_playbook_execution(self):
        self.platform.register_agent(self.tenant, self.agent_id, self.agent_info)
        self.platform.add_route(self.tenant, 'taskX', self.agent_id)
        self.assertEqual(self.platform.get_route(self.tenant, 'taskX'), self.agent_id)
        self.platform.add_playbook(self.tenant, 'pb1', dummy_playbook)
        result = self.platform.run_playbook(self.tenant, 'pb1', {'x': 41})
        self.assertEqual(result, {'y': 42})

    def test_policy_enforcement_denied(self):
        self.platform.register_agent(self.tenant, self.agent_id, self.agent_info)
        self.platform.add_playbook(self.tenant, 'pb2', dummy_playbook)
        self.platform.set_policy(self.tenant, 'run_playbook', deny_all)
        with self.assertRaises(PermissionDenied):
            self.platform.run_playbook(self.tenant, 'pb2', {'x': 1})

    def test_tenant_isolation(self):
        self.platform.register_agent('tenantA', 'agentA', {'name': 'A'})
        self.platform.register_agent('tenantB', 'agentB', {'name': 'B'})
        # Cross-tenant access should be denied
        with self.assertRaises(PermissionDenied):
            self.platform.cross_tenant_get_agent('tenantA', 'tenantB', 'agentB')
        # Same-tenant access should succeed
        agent = self.platform.cross_tenant_get_agent('tenantA', 'tenantA', 'agentA')
        self.assertEqual(agent, {'name': 'A'})

    def test_not_found_errors(self):
        # Getting non-existent agent
        with self.assertRaises(NotFound):
            self.platform.get_agent(self.tenant, 'noagent')
        # Getting non-existent route
        with self.assertRaises(NotFound):
            self.platform.get_route(self.tenant, 'no_task')
        # Getting non-existent playbook
        with self.assertRaises(NotFound):
            self.platform.run_playbook(self.tenant, 'no_pb', {})
        # Getting non-existent profile
        self.platform.register_agent(self.tenant, self.agent_id, self.agent_info)
        with self.assertRaises(NotFound):
            self.platform.get_profile(self.tenant, self.agent_id)

