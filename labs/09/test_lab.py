# test_lab.py
import unittest
from main import dispatch

def make_handler(result=None, delegate_to=None):
    def handler(task):
        if delegate_to is not None:
            return {'delegate_to': delegate_to}
        return result if result is not None else {'echo': task['payload']}
    return handler

class TestHierarchicalOrchestrator(unittest.TestCase):
    def setUp(self):
        self.profiles = {
            'root': {
                'handler': make_handler(delegate_to='alpha'),
                'delegates': ['alpha', 'beta']
            },
            'alpha': {
                'handler': make_handler(result={'done': 'alpha'}),
                'delegates': []
            },
            'beta': {
                'handler': make_handler(result={'done': 'beta'}),
                'delegates': []
            },
        }

    def test_simple_delegation(self):
        task = {'domain': 'root', 'payload': 'work'}
        result = dispatch(task, self.profiles)
        self.assertEqual(result['domain'], 'root')
        self.assertIsNone(result['result'])
        self.assertEqual(result['delegated']['domain'], 'alpha')
        self.assertEqual(result['delegated']['result'], {'done': 'alpha'})
        self.assertIsNone(result['delegated']['delegated'])

    def test_no_delegation(self):
        task = {'domain': 'alpha', 'payload': 'work'}
        result = dispatch(task, self.profiles)
        self.assertEqual(result['domain'], 'alpha')
        self.assertEqual(result['result'], {'done': 'alpha'})
        self.assertIsNone(result['delegated'])

    def test_permission_denied_on_delegation(self):
        # alpha tries to delegate to beta, but is not allowed
        profiles = dict(self.profiles)
        profiles['alpha'] = {
            'handler': make_handler(delegate_to='beta'),
            'delegates': []  # not allowed
        }
        task = {'domain': 'alpha', 'payload': 'work'}
        with self.assertRaises(PermissionError):
            dispatch(task, profiles)

    def test_cyclic_delegation_detected(self):
        # root delegates to alpha, alpha delegates back to root
        profiles = dict(self.profiles)
        profiles['alpha'] = {
            'handler': make_handler(delegate_to='root'),
            'delegates': ['root']
        }
        task = {'domain': 'root', 'payload': 'work'}
        with self.assertRaises(RuntimeError):
            dispatch(task, profiles)

    def test_missing_domain(self):
        task = {'domain': 'missing', 'payload': 'work'}
        with self.assertRaises(ValueError):
            dispatch(task, self.profiles)

    def test_invalid_handler(self):
        profiles = dict(self.profiles)
        profiles['alpha'] = {
            'handler': None,
            'delegates': []
        }
        task = {'domain': 'alpha', 'payload': 'work'}
        with self.assertRaises(ValueError):
            dispatch(task, profiles)

    def test_invalid_task_type(self):
        with self.assertRaises(TypeError):
            dispatch('notadict', self.profiles)

    def test_invalid_profiles_type(self):
        task = {'domain': 'root', 'payload': 'work'}
        with self.assertRaises(TypeError):
            dispatch(task, 'notadict')

    def test_missing_task_keys(self):
        with self.assertRaises(ValueError):
            dispatch({'domain': 'root'}, self.profiles)
        with self.assertRaises(ValueError):
            dispatch({'payload': 'work'}, self.profiles)

if __name__ == '__main__':
    unittest.main()

