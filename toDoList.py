"""
Using this to plan my week for classes.
Todo:
    Error handling -- if anything is corrupt in json file, it breaks
    sort by done at top -- this will require a change in data structure
"""
import json
import os

from colorama import init, Fore

import data_management
import strings
import celebrate
import initial_build
import show_list


########################################################################################################################
# The main program
########################################################################################################################


def main(week_number, assignments_due):
    init()
    while True:
        os.system(strings.CLS)
        to_do_list = show_list.text_display(assignments_due, week_number)
        print(f'{Fore.CYAN}{strings.TITLE}{Fore.RESET}')
        print(to_do_list)
        option = input(strings.OPTIONS)
        os.system(strings.CLS)
        if option.lower() == 'm':
            week_number, assignments_due = initial_build.build()

        elif option.lower() == 'a':
            try:
                item_to_add, date_due = data_management.append_items()
                assignments_due[item_to_add] = date_due
            except TypeError:
                continue

        elif option.lower() == 'e':
            item_to_edit = data_management.show_assignments(assignments_due)

            # {item_to_do: [due_date, bool_indicating_status]}
            # confusing, idk a better way
            # please for the love of god find a better way
            if not item_to_edit:
                continue
            else:
                assignments_due[item_to_edit][1] = data_management.change_state(assignments_due[item_to_edit][1])

            if data_management.check_complete(assignments_due):
                celebrate.finished(week_number)

        elif option.lower() == 'd':
            data_management.delete_item(assignments_due)

        elif option.lower() == 'q':
            break

        else:
            print(f'\n\n\n{Fore.RED}Error: Invalid option{Fore.RESET}')

    return week_number, assignments_due


if __name__ == '__main__':
    try:
        with open(strings.OUTPUT_FILE, 'r') as file:
            json_data = json.load(file)

        week_num = json_data[0]
        assignments = json_data[1]

    except FileNotFoundError:
        week_num = 'WEEK --'
        assignments = {}

    week_num, assignments = main(week_num, assignments)

    json_data = [week_num, assignments]
    with open(strings.OUTPUT_FILE, 'w') as file:
        json.dump(json_data, file, indent=4)
