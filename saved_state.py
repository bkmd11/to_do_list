import json

with open('main_list.json', 'r') as file:
    saved_state = json.load(file)


def text_display():
    """This is the display that shows what is due this week"""
    count = 1
    print(f'ASSIGNMENTS DUE FOR {saved_state[0]}')
    for assignment, due_date in saved_state[1].items():
        print(f'{count}: {assignment} \n\t- {due_date}\n')
        count += 1
