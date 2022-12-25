import strings


"""I am what builds out the strings to show text on the list"""


def text_display(assignment_dict, week_number):
    """This is the display that shows what is due this week"""
    sorted_dict = dict(sorted(assignment_dict.items(), key=day_index))
    todo_list = f'{strings.ASSIGNMENT_MESSAGE} {week_number}'
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
    index = strings.DAYS.index(day[1][0].capitalize())

    return index
