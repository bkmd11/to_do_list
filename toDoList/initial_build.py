from toDoList import strings

"""I am what builds out the initial list"""


def input_week():
    """Takes user input for what week of the course it is"""
    week_number = input(strings.INPUT_MESSAGE)

    if week_number == strings.COURSE_LENGTH:
        return strings.LAST_WEEK_STRING

    else:
        return f'{strings.WEEK} {week_number}'


def input_assignments():
    """ Takes user input to create a dictionary of tasks with their due dates as values"""

    assignment_dictionary = {}
    while True:
        assignments_to_do = input(strings.BUILD_MESSAGE).capitalize()
        if assignments_to_do == '':
            break
        due_date = input(strings.WHEN_DUE).capitalize()

        if due_date in strings.DAYS:
            assignment_dictionary[assignments_to_do] = [due_date, False]
        else:
            print(strings.DAY_ERROR_MESSAGE)

    return assignment_dictionary


def build():
    """ Saves the week int and assignment dict as a list in json"""
    week = input_week()
    items_due = input_assignments()

    return week, items_due