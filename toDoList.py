#! python3
"""takes input and makes a .txt file.
Using this to plan my week for classes.
Todo: make this a cli tool that loads json data and displays my list for the week
    and allows me to add DONE when I finish something.
    This will have argeparse to make, view, and edit
    And possibly sexy  colors for various things
"""


# Takes input for what needs to get done
def task_manager(assignment, due_date, dictionary):
    dictionary[assignment] = due_date

    return dictionary


# Takes that input and puts it into a dict      
def make_list(dictionary):
    count = 1
    main_string = ''

    for assingnment, due_date in dictionary.items():
        string = f'{count}: {assingnment}\n   - {due_date}\n'
        count += 1
        main_string += string
    return str(main_string)


def main():
    # takes input for list
    week_number = input('What week is this?\n')

    if week_number == '8':
        week_number = 'THE LAST FUCKING WEEK OF THIS SHITTY SHIT!!!'

    else:
        week_number = f'WEEK {week_number}'

    assignment_dictionary = {}
    while True:
        assignments = input('What assignments are due this week?\nEnter nothing to quit\n')
        if assignments == '':
            break
        due_date = input('When is this due?\n')

        assignment_dictionary = task_manager(assignments, due_date, assignment_dictionary)

    main_list = make_list(assignment_dictionary)

    # makes a numbered list and saves it to a file
    my_list=open('C:\\Users\\Brian Kendall\\Desktop\\School Assignments.txt', 'w')
    my_list.write(f'ASSIGNMENTS DUE FOR {week_number}:\n\n')
    my_list.write(main_list)

    my_list.close()


if __name__ == '__main__':
    main()



