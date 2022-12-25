"""
Using this to plan my week for classes.
Todo:
    Error handling -- if anything is corrupt in json file, it breaks
    sort by done at top -- this will require a change in data structure
    Refactor into better structure with different files to manage better
"""
import json
import os
import random
import time

from colorama import init, Fore, Style


########################################################################################################################
# Global variables because I suck
########################################################################################################################


OPTIONS = '\nOptions:\n(m) make new list\n(a) add an item\n(e) edit the list\n(d) delete item\n(q) quit\n'
LAST_WEEK_STRING = 'THE LAST FUCKING WEEK OF THIS SHITTY SHIT!!!'
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAY_ERROR_MESSAGE = 'That is not a valid day, please re-input assignment\n'
INT_ERROR = 'please input valid number\n'
COURSE_LENGTH = '7'
CLS = 'cls'
WHEN_DUE = 'When is this due?\n'
BUILD_MESSAGE = 'What assignments are due this week?\nEnter nothing to quit\n'
UPDATE_ASSIGNMENT = 'Enter the number of the assignment to update, or leave blank to exit:\n '
DELETE_MESSAGE = 'Enter the number of the assignment to delete: '
ASSIGNMENT_MESSAGE = 'ASSIGNMENTS DUE FOR'
TITLE = 'TODO LIST'
INPUT_MESSAGE = 'What week is this?\n'
WEEK = 'WEEK'
OUTPUT_FILE = 'main_list.json'

########################################################################################################################
# This portion focuses on making the list
########################################################################################################################


def input_week():
    """Takes user input for what week of the course it is"""
    week_number = input(INPUT_MESSAGE)

    if week_number == COURSE_LENGTH:
        return LAST_WEEK_STRING

    else:
        return f'{WEEK} {week_number}'


def input_assignments():
    """ Takes user input to create a dictionary of tasks with their due dates as values"""

    assignment_dictionary = {}
    while True:
        assignments_to_do = input(BUILD_MESSAGE)
        if assignments_to_do == '':
            break
        due_date = input(WHEN_DUE).capitalize()

        if due_date in DAYS:
            assignment_dictionary[assignments_to_do] = [due_date, False]
        else:
            print(DAY_ERROR_MESSAGE)

    return assignment_dictionary


def build():
    """ Saves the week int and assignment dict as a list in json"""
    week = input_week()
    items_due = input_assignments()

    return week, items_due

########################################################################################################################
# This portion shows the list
########################################################################################################################


def text_display(assignment_dict, week_number):
    """This is the display that shows what is due this week"""
    sorted_dict = dict(sorted(assignment_dict.items(), key=day_index))
    todo_list = f'{ASSIGNMENT_MESSAGE} {week_number}'
    count = 1
    for assignment, due_date in sorted_dict.items():
        if due_date[1] is False:
            todo_list += f'\n{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.RESET}'
        else:
            todo_list += f'\n{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.GREEN}DONE!{Fore.RESET}'
        count += 1

    return todo_list


def day_index(day):
    """I return an index for the day list so the text display is in order"""
    index = DAYS.index(day[1][0].capitalize())

    return index
########################################################################################################################
# This portion edits the data in the json file
########################################################################################################################


def show_assignments(assignment_dict):
    """ Shows a list of the assignments with a reference number"""
    sorted_dict = dict(sorted(assignment_dict.items(), key=day_index))

    while True:
        items = [i for i in sorted_dict.keys()]
        for i in items:
            if assignment_dict[i][1]:
                print(f'{Fore.GREEN}{items.index(i) + 1}: {i}{Fore.RESET}')
            else:
                print(f'{Fore.RED}{items.index(i) + 1}: {i}{Fore.RESET}')

        index = input(UPDATE_ASSIGNMENT)
        if index == '':
            break
        try:
            return items[int(index) - 1]
        except IndexError as e:
            print(f'{e} {INT_ERROR}')
        except ValueError as e:
            print(f'{e} {INT_ERROR}')


def change_state(due_date_bool):
    """ Changes the state of the assignment to toggle complete and incomplete
        False means task is not done, True means it is complete"""
    if due_date_bool:
        return False
    else:
        return True


def append_items():
    """Adds items to the list"""
    while True:
        assignments_to_do = input(BUILD_MESSAGE)
        if assignments_to_do == '':
            break
        due_date = input(WHEN_DUE).capitalize()

        if due_date in DAYS:
            return assignments_to_do, [due_date, False]

        else:
            print(DAY_ERROR_MESSAGE)


def check_complete(assignments_due):
    """Compares the boolean value of all assignments to see if they are done"""
    for i in assignments_due.values():
        if i[1] is False:
            return False

    return True


def delete_item(assignment_dict):
    """Deletes an item from the list to fix mistakes"""
    items = [i for i in assignment_dict.keys()]
    for i in items:
        print(f'{items.index(i) + 1}: {i}')

    index = int(input(DELETE_MESSAGE))

    assignment_dict.pop(items[index - 1])


########################################################################################################################
# Something fun when I finish a week/class
########################################################################################################################
def finished(week):
    """I take a week and figure out if it is the last week, then return a function"""
    if week == LAST_WEEK_STRING:
        finished_class()
    else:
        finished_week()


def finished_week():
    """ Prints a fun message when I finish all assignments"""
    os.system(CLS)
    colors = list(vars(Fore).values())
    count = 0
    while count != 11:
        time.sleep(1)
        print(' ' * random.randint(0, 100), end='')
        print(
            f'{Style.BRIGHT}{random.choice(colors)}Another '
            f'{random.choice(colors)}Week '
            f'{random.choice(colors)}Complete! ', end=''
        )
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} *', end='')
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} **')
        count += 1


def finished_class():
    # Todo: add credit countdown
    """ Prints a fun message when I finish a class"""
    os.system(CLS)
    colors = list(vars(Fore).values())
    count = 0
    while count != 11:
        time.sleep(1)
        print(' ' * random.randint(0, 100), end='')
        print(
            f'{Style.BRIGHT}{random.choice(colors)}  One   '
            f'{random.choice(colors)} Step '
            f'{random.choice(colors)}   Closer! ', end=''
        )
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} *', end='')
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} **')

        count += 1

########################################################################################################################
# The main program
########################################################################################################################


def main(week_number, assignments_due):
    init()
    while True:
        os.system(CLS)
        to_do_list = text_display(assignments_due, week_number)
        print(f'{Fore.CYAN}{TITLE}{Fore.RESET}')
        print(to_do_list)
        option = input(OPTIONS)
        os.system(CLS)
        if option.lower() == 'm':
            week_number, assignments_due = build()

        elif option.lower() == 'a':
            try:
                item_to_add, date_due = append_items()
                assignments_due[item_to_add] = date_due
            except TypeError:
                continue

        elif option.lower() == 'e':
            item_to_edit = show_assignments(assignments_due)

            # {item_to_do: [due_date, bool_indicating_status]}
            # confusing, idk a better way
            # please for the love of god find a better way
            if not item_to_edit:
                continue
            else:
                assignments_due[item_to_edit][1] = change_state(assignments_due[item_to_edit][1])

            if check_complete(assignments_due):
                finished(week_number)

        elif option.lower() == 'd':
            delete_item(assignments_due)

        elif option.lower() == 'q':
            break

        else:
            print(f'\n\n\n{Fore.RED}Error: Invalid option{Fore.RESET}')

    return week_number, assignments_due


if __name__ == '__main__':
    try:
        with open(OUTPUT_FILE, 'r') as file:
            json_data = json.load(file)

        week_num = json_data[0]
        assignments = json_data[1]

    except FileNotFoundError:
        week_num = 'WEEK --'
        assignments = {}

    week_num, assignments = main(week_num, assignments)

    json_data = [week_num, assignments]
    with open(OUTPUT_FILE, 'w') as file:
        json.dump(json_data, file, indent=4)
