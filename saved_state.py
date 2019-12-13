import json


def text_display():
    """This is the display that shows what is due this week"""
    with open('main_list.json', 'r') as file:
        saved_state = json.load(file)

    count = 1

    print(f'ASSIGNMENTS DUE FOR {saved_state[0]}')
    for assignment, due_date in saved_state[1].items():
        if due_date[1] is False:
            print(f'{count}: {assignment} \n\t- {due_date[0]}\n')
        else:
            print(f'{count}: {assignment} - {due_date[0]}\nDONE!')
        count += 1

text_display()