#! python3
"""takes input and makes a .txt file.
Using this to plan my week for classes.
Todo: make this a cli tool that loads json data and displays my list for the week
    and allows me to add DONE when I finish something.
    This will have argeparse to make, view, and edit
    And possibly sexy  colors for various things
"""

import pysnooper
import json


def input_week():
    """Takes user input for what week of the course it is"""
    week_number = input('What week is this?\n')

    if week_number == '8':
        return 'THE LAST FUCKING WEEK OF THIS SHITTY SHIT!!!'

    else:
        return f'WEEK {week_number}'


def input_assignments():
    """ Takes user input to create a dictionary of tasks with their due dates as values"""
    assignment_dictionary = {}
    while True:
        assignments = input('What assignments are due this week?\nEnter nothing to quit\n')
        if assignments == '':
            break
        due_date = input('When is this due?\n')

        assignment_dictionary[assignments] = due_date

    return assignment_dictionary


def build():
    """ Saves the week int and assignment dict as a list in json"""
    week = input_week()
    items_due = input_assignments()
    with open('main_list.json', 'w') as file:
        json.dump([week, items_due], file)


if __name__ == '__main__':
    build()

