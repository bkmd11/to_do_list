import unittest
import unittest.mock

import tools


# Todo: I broke my tests like a fool


class TestInputWeek(unittest.TestCase):
    def test_input_week_string_number(self):
        """Testing for string input of number"""
        with unittest.mock.patch('builtins.input', return_value='2'):
            self.assertEqual(tools.input_week(), 'WEEK 2')

    def test_input_week_string_word(self):
        """Testing for string input of text"""
        with unittest.mock.patch('builtins.input', return_value='Two'):
            self.assertEqual(tools.input_week(), 'WEEK Two')

    def test_input_week_eight(self):
        """Testing for week 8"""
        with unittest.mock.patch('builtins.input', return_value='8'):
            self.assertEqual(tools.input_week(), 'THE LAST FUCKING WEEK OF THIS SHITTY SHIT!!!')

    def test_input_week_int(self):
        """Testing for int input"""
        with unittest.mock.patch('builtins.input', return_value=2):
            self.assertEqual(tools.input_week(), 'WEEK 2')


class TestShowAssignments(unittest.TestCase):
    def test_show_assignments_index(self):
        """Testing that show_assignments will index properly"""
        with unittest.mock.patch('builtins.input', return_value=1):
            self.assertEqual(tools.show_assignments({'spam': False, 'eggs': False}), 'spam')

    def test_show_assignments_index_string(self):
        """Testing that a string number gets converted to an integer"""
        with unittest.mock.patch('builtins.input', return_value='1'):
            self.assertEqual(tools.show_assignments({'spam': False, 'eggs': False}), 'spam')


class TestChangeState(unittest.TestCase):
    def test_change_state_true(self):
        """Tests from false to true"""
        self.assertFalse(tools.change_state(True))

    def test_change_state_false(self):
        """Tests from true to false"""
        self.assertTrue(tools.change_state(False))


class TestAppendItems(unittest.TestCase):
    def test_append_items(self):
        """Testing items get put in the tuple correctly, and list gets made correctly"""
        with unittest.mock.patch('builtins.input', side_effect=['Spam', 'eggs']):
            self.assertEqual(tools.append_items(), ('Spam', ['eggs', False]))

    def test_append_items_handles_blanks(self):
        """Testing empty input values"""
        with unittest.mock.patch('builtins.input', side_effect=['Spam', '']):
            self.assertEqual(tools.append_items(), ('Spam', ['', False]))


class TestInputAssignments(unittest.TestCase):
    def test_input_assignments_loops_once(self):
        """Testing input_assignments makes dictionary correctly, loops through once"""
        with unittest.mock.patch('builtins.input', side_effect=['spam', 'eggs', '']):
            self.assertEqual(tools.input_assignments(), {'spam': ['eggs', False]})

    def test_input_assignments_loops_multiple(self):
        """Testing input_assignments will loop through multiple times"""
        with unittest.mock.patch('builtins.input', side_effect=['spam', 'eggs', 'foo', 'bar', '']):
            self.assertEqual(tools.input_assignments(), {'spam': ['eggs', False], 'foo': ['bar', False]})


class TestCheckComplete(unittest.TestCase):
    def test_check_complete_true(self):
        """Testing that the loop will return true if value true"""
        self.assertTrue(tools.check_complete({'spam': ['eggs', True], 'eggs': ['spam', True]}))

    def test_check_complete_false(self):
        """Testing that the loop will break at false"""
        self.assertFalse(tools.check_complete({'spam': ['eggs', False], 'eggs': ['spam', True]}))

    def test_check_complete_false_not_first(self):
        """Testing that it wont just return the first true"""
        self.assertFalse(tools.check_complete({'spam': ['eggs', True], 'eggs': ['spam', False]}))


if __name__ == '__main__':
    unittest.main(buffer=True)
