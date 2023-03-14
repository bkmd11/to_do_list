import unittest

from toDoList import data_management


class TestChangeState(unittest.TestCase):
    def test_true_to_false(self):
        self.assertTrue(data_management.change_state(False))

    def test_false_to_true(self):
        self.assertFalse(data_management.change_state(True))


class TestCheckComplete(unittest.TestCase):
    def test_assignments_done(self):
        self.assertTrue(data_management.check_complete({'spam': ['mon', True], 'eggs': ['tue', True]}))

    def test_assignments_not_done(self):
        self.assertFalse(data_management.check_complete({'spam': ['mon', True], 'eggs': ['tue', False]}))