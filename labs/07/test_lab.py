# test_lab.py
import unittest
from main import run_playbook, PlaybookExecutionError, PlaybookCycleError

def dummy_action(**kwargs):
    return True

def always_fail_action(**kwargs):
    return False

def check_true(**kwargs):
    return True

def check_false(**kwargs):
    return False

def raise_error(**kwargs):
    raise RuntimeError("Intentional error")

class TestPlaybookExecutionEngine(unittest.TestCase):
    def setUp(self):
        self.tools = {
            'do': dummy_action,
            'fail': always_fail_action,
            'check_true': check_true,
            'check_false': check_false,
            'raise_error': raise_error
        }

    def test_successful_playbook(self):
        playbook = [
            {'id': 'step1', 'action': 'do', 'args': {}, 'checks': [{'action': 'check_true'}]},
            {'id': 'step2', 'action': 'do', 'args': {}, 'checks': [{'action': 'check_true'}]}
        ]
        result = run_playbook(playbook, self.tools)
        self.assertEqual(result['steps'], {'step1': 'success', 'step2': 'success'})
        self.assertIsNone(result['failed_step'])

    def test_step_with_retry_and_failure(self):
        playbook = [
            {'id': 'step1', 'action': 'fail', 'args': {}, 'checks': [{'action': 'check_false'}], 'retries': 2, 'on_failure': 'step2'},
            {'id': 'step2', 'action': 'do', 'args': {}, 'checks': [{'action': 'check_true'}]}
        ]
        result = run_playbook(playbook, self.tools)
        self.assertEqual(result['steps']['step1'], 'failed')
        self.assertEqual(result['steps']['step2'], 'success')
        self.assertEqual(result['failed_step'], 'step1')

    def test_cycle_detection(self):
        playbook = [
            {'id': 'a', 'action': 'do', 'on_failure': 'b'},
            {'id': 'b', 'action': 'fail', 'on_failure': 'a'}
        ]
        with self.assertRaises(PlaybookCycleError):
            run_playbook(playbook, self.tools)

    def test_action_error_handling_and_bounded_retry(self):
        playbook = [
            {'id': 'err', 'action': 'raise_error', 'retries': 1, 'checks': []}
        ]
        result = run_playbook(playbook, self.tools)
        self.assertEqual(result['steps']['err'], 'failed')
        self.assertEqual(result['failed_step'], 'err')

    def test_duplicate_step_id(self):
        playbook = [
            {'id': 'dup', 'action': 'do'},
            {'id': 'dup', 'action': 'do'}
        ]
        with self.assertRaises(ValueError):
            run_playbook(playbook, self.tools)

    def test_unknown_action(self):
        playbook = [
            {'id': 'x', 'action': 'not_a_tool'}
        ]
        result = run_playbook(playbook, self.tools)
        self.assertEqual(result['steps']['x'], 'failed')
        self.assertEqual(result['failed_step'], 'x')

if __name__ == '__main__':
    unittest.main()




