"""takes input and makes a .txt file.
Using this to plan my week for classes.
Todo:
    Error handling
    possibly sexy  colors for various things
"""
import json
import os


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

    return [week, items_due]

########################################################################################################################
# This portion shows the list
########################################################################################################################


def text_display(assignment_dict):
    """This is the display that shows what is due this week"""
    print(f'ASSIGNMENTS DUE FOR {assignment_dict[0]}')
    count = 1
    for assignment, due_date in assignment_dict[1].items():
        if due_date[1] is False:
            print(f'{count}: {assignment} \n\t- {due_date[0]}\n')
        else:
            print(f'{count}: {assignment} - {due_date[0]}\nDONE!')
        count += 1

########################################################################################################################
# This portion edits the data in the json file
########################################################################################################################


def show_assignments(assignment_dict):
    """ Shows a list of the assignments with a reference number"""
    items = [i for i in assignment_dict[1].keys()]
    for i in items:
        print(f'{items.index(i)}: {i}')

    index = int(input('Enter the number of the finished assignment: '))     # Should do this somewhere else
    return items[index]


def change_state(dict_key, assignment_dict):
    """ Changes the state of the assignment to True to indicate that an assignment is done"""
    assignment_dict[1][dict_key][1] = True          # This is confusing as shit
    print('Assignment marked as complete!')

########################################################################################################################
# The main program
########################################################################################################################


def main():
    with open('main_list.json', 'r') as file:
        assignments = json.load(file)
    print('TODO LIST')
    while True:
        option = input('\nOptions:\n(m) make the list,\n(e) edit the list,\n(v) view the list\n(q) quit\n')
        os.system('cls')
        if option.lower() == 'm':
            assignments = build()
            os.system('cls')

        elif option.lower() == 'e':
            item_to_edit = show_assignments(assignments)
            change_state(item_to_edit, assignments)

        elif option.lower() == 'v':
            text_display(assignments)

        elif option.lower() == 'q':
            break

        else:
            print('Error: Invalid option')

    with open('main_list.json', 'w') as file:
        json.dump(assignments, file, indent=4)


if __name__ == '__main__':
    main()
