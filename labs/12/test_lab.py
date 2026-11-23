# test_lab.py
import unittest
from main import evaluate

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def adapter_passthrough(task_name, input_dict):
    # Simulates a proxy that just calls the registry function
    if task_name == 'add':
        return add(**input_dict)
    elif task_name == 'mul':
        return mul(**input_dict)
    else:
        raise ValueError('Unknown task')

def adapter_offset(task_name, input_dict):
    # Simulates an adapter that adds 1 to the result
    if task_name == 'add':
        return add(**input_dict) + 1
    elif task_name == 'mul':
        return mul(**input_dict) + 1
    else:
        raise ValueError('Unknown task')

class TestSkillScalabilityBenchmark(unittest.TestCase):
    def setUp(self):
        self.registry = {'add': add, 'mul': mul}
        self.tasks = [
            {'name': 'add', 'input': {'a': 2, 'b': 3}},
            {'name': 'mul', 'input': {'a': 2, 'b': 3}},
        ]
        self.adapters = {
            'passthrough': adapter_passthrough,
            'offset': adapter_offset
        }

    def test_proxy_and_real_results(self):
        results = evaluate(self.registry, self.tasks, self.adapters)
        # Check real results
        self.assertEqual(results['real']['add']['result'], 5)
        self.assertEqual(results['real']['mul']['result'], 6)
        # Check proxy results
        self.assertEqual(results['proxy']['passthrough']['add']['result'], 5)
        self.assertEqual(results['proxy']['passthrough']['mul']['result'], 6)
        self.assertEqual(results['proxy']['offset']['add']['result'], 6)
        self.assertEqual(results['proxy']['offset']['mul']['result'], 7)

    def test_missing_task_in_registry(self):
        tasks = self.tasks + [{'name': 'sub', 'input': {'a': 1, 'b': 1}}]
        results = evaluate(self.registry, tasks, self.adapters)
        self.assertIn('error', results['real']['sub'])
        self.assertEqual(results['real']['sub']['error'], 'Task not in registry')
        # Adapters should raise error for unknown task
        self.assertIn('error', results['proxy']['passthrough']['sub'])
        self.assertIn('Unknown task', results['proxy']['passthrough']['sub']['error'])

    def test_empty_tasks_and_adapters(self):
        results = evaluate(self.registry, [], {})
        self.assertEqual(results['tasks'], [])
        self.assertEqual(results['adapters'], [])
        self.assertEqual(results['real'], {})
        self.assertEqual(results['proxy'], {})

    def test_adapter_exception_handling(self):
        def bad_adapter(task_name, input_dict):
            raise RuntimeError('Adapter failed')
        adapters = {'bad': bad_adapter}
        results = evaluate(self.registry, self.tasks, adapters)
        for task in self.tasks:
            self.assertIn('error', results['proxy']['bad'][task['name']])
            self.assertIn('Adapter failed', results['proxy']['bad'][task['name']]['error'])

if __name__ == '__main__':
    unittest.main()

