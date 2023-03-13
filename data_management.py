from colorama import Fore

import strings
import show_list

"""I manipulate data from the fucked up list"""


def show_assignments(assignment_dict):
    """ Shows a list of the assignments with a reference number"""
    sorted_dict = dict(sorted(assignment_dict.items(), key=show_list.day_index))

    while True:
        items = [i for i in sorted_dict.keys()]
        for i in items:
            if assignment_dict[i][1]:
                print(f'{Fore.GREEN}{items.index(i) + 1}: {i}{Fore.RESET}')
            else:
                print(f'{Fore.RED}{items.index(i) + 1}: {i}{Fore.RESET}')

        index = input(strings.UPDATE_ASSIGNMENT)
        if index == '':
            break
        try:
            return items[int(index) - 1]
        except IndexError as e:
            print(f'{e} {strings.INT_ERROR}')
        except ValueError as e:
            print(f'{e} {strings.INT_ERROR}')


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
        assignments_to_do = input(strings.BUILD_MESSAGE)
        if assignments_to_do == '':
            break
        due_date = input(strings.WHEN_DUE).capitalize()

        if due_date in strings.DAYS:
            return assignments_to_do, [due_date, False]

        else:
            print(strings.DAY_ERROR_MESSAGE)


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

    index = int(input(strings.DELETE_MESSAGE))

    assignment_dict.pop(items[index - 1])
