import unittest

import data_management


class TestChangeState(unittest.TestCase):
    def test_true_to_false(self):
        self.assertTrue(data_management.change_state(False))

    def test_false_to_true(self):
        self.assertFalse(data_management.change_state(True))
