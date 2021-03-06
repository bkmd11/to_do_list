"""takes input and makes a .txt file.
Using this to plan my week for classes.
Todo:
    Error handling -- if anything is corrupt in json file, it breaks
"""
import json
import os

from colorama import init, Fore


########################################################################################################################
# This portion focuses on making the list
########################################################################################################################
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
        assignments_to_do = input('What assignments are due this week?\nEnter nothing to quit\n')
        if assignments_to_do == '':
            break
        due_date = input('When is this due?\n')

        assignment_dictionary[assignments_to_do] = [due_date, False]

    return assignment_dictionary


def build():
    # TODO: integration test to assure the right format is returned
    """ Saves the week int and assignment dict as a list in json"""
    week = input_week()
    items_due = input_assignments()

    return week, items_due

########################################################################################################################
# This portion shows the list
# TODO: Could add a feature to print off notes that I add
########################################################################################################################


def text_display(assignment_dict, week_number):
    # TODO: write tests
    """This is the display that shows what is due this week"""
    todo_list = f'ASSIGNMENTS DUE FOR {week_number}'
    count = 1
    for assignment, due_date in assignment_dict.items():
        if due_date[1] is False:
            todo_list += f'\n{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.RESET}'
        else:
            todo_list += f'\n{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.GREEN}DONE!{Fore.RESET}'
        count += 1

    return todo_list

########################################################################################################################
# This portion edits the data in the json file
########################################################################################################################


def show_assignments(assignment_dict):
    """ Shows a list of the assignments with a reference number"""
    items = [i for i in assignment_dict.keys()]
    for i in items:
        print(f'{items.index(i) + 1}: {i}')

    index = int(input('Enter the number of the assignment to update: '))
    return items[index - 1]


def change_state(due_date_bool):
    """ Changes the state of the assignment to toggle complete and incomplete
        False means task is not done, True means it is complete"""
    if due_date_bool:
        return False
    else:
        return True


def append_items():
    """Adds items to the list"""
    assignments_to_do = input('What are you adding to the list?\n')
    due_date = input('When is this due?\n')

    return assignments_to_do, [due_date, False]

########################################################################################################################
# The main program
########################################################################################################################


def main(week_number, assignments_due):
    init()
    while True:
        os.system('cls')
        to_do_list = text_display(assignments_due, week_number)
        print(f'{Fore.CYAN}TODO LIST{Fore.RESET}')
        print(to_do_list)
        option = input(
            '\nOptions:\n(m) make new list\n(a) add an item\n(e) edit the list\n(q) quit\n')
        os.system('cls')
        if option.lower() == 'm':
            week_number, assignments_due = build()

        elif option.lower() == 'a':
            item_to_add, date_due = append_items()
            assignments_due[item_to_add] = date_due

        elif option.lower() == 'e':
            item_to_edit = show_assignments(assignments_due)

            # {item_to_do: [due_date, bool_indicating_status]}
            # confusing, idk a better way
            assignments_due[item_to_edit][1] = change_state(assignments_due[item_to_edit][1])

        elif option.lower() == 'q':
            break

        else:
            print(f'\n\n\n{Fore.RED}Error: Invalid option{Fore.RESET}')

    return week_number, assignments_due


if __name__ == '__main__':
    try:
        with open('main_list.json', 'r') as file:
            json_data = json.load(file)

        week_num = json_data[0]
        assignments = json_data[1]

    except FileNotFoundError:
        week_num = 'WEEK --'
        assignments = {}

    week_num, assignments = main(week_num, assignments)

    json_data = [week_num, assignments]
    with open('main_list.json', 'w') as file:
        json.dump(json_data, file, indent=4)
