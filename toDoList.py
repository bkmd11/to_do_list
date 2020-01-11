"""takes input and makes a .txt file.
Using this to plan my week for classes.
Todo:
    Error handling -- if anything is corrupt in json file, it breaks
    write tests
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
        assignments = input('What assignments are due this week?\nEnter nothing to quit\n')
        if assignments == '':
            break
        due_date = input('When is this due?\n')

        assignment_dictionary[assignments] = [due_date, False]

    return assignment_dictionary


def build():
    """ Saves the week int and assignment dict as a list in json"""
    week = input_week()
    items_due = input_assignments()

    return week, items_due

########################################################################################################################
# This portion shows the list
# TODO: Could add a feature to print off notes that I add
########################################################################################################################


def text_display(assignment_dict, week_number):
    """This is the display that shows what is due this week"""
    print(f'ASSIGNMENTS DUE FOR {week_number}')
    count = 1
    for assignment, due_date in assignment_dict.items():
        if due_date[1] is False:
            print(f'{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.RESET}')
        else:
            print(f'{count}: {assignment} \n{Fore.RED}\t- {due_date[0]}\n{Fore.GREEN}DONE!{Fore.RESET}')
        count += 1


########################################################################################################################
# This portion edits the data in the json file
########################################################################################################################


def show_assignments(assignment_dict):
    """ Shows a list of the assignments with a reference number"""
    items = [i for i in assignment_dict.keys()]
    for i in items:
        print(f'{items.index(i) + 1}: {i}')

    index = int(input('Enter the number of the finished assignment: '))
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
    assignments = input('What are you adding to the list?\n')
    due_date = input('When is this due?\n')

    return assignments, [due_date, False]

########################################################################################################################
# The main program
########################################################################################################################


def main():
    init()
    with open('main_list.json', 'r') as file:
        json_data = json.load(file)

    week_num = json_data[0]
    assignments = json_data[1]

    while True:
        os.system('cls')
        print(f'{Fore.CYAN}TODO LIST{Fore.RESET}')
        text_display(assignments, week_num)
        option = input(
            '\nOptions:\n(m) make new list\n(a) add an item\n(e) edit the list\n(q) quit\n')
        os.system('cls')
        if option.lower() == 'm':
            week_num, assignments = build()

        elif option.lower() == 'a':
            item_to_add, date_due = append_items()
            assignments[item_to_add] = date_due

        elif option.lower() == 'e':
            item_to_edit = show_assignments(assignments)

            # {item_to_do: [due_date, bool_indicating_status]}
            # confusing, idk a better way
            assignments[item_to_edit][1] = change_state(assignments[item_to_edit][1])

        elif option.lower() == 'q':
            break

        else:
            print(f'\n\n\n{Fore.RED}Error: Invalid option{Fore.RESET}')

    json_data = [week_num, assignments]
    with open('main_list.json', 'w') as file:
        json.dump(json_data, file, indent=4)


if __name__ == '__main__':
    main()
