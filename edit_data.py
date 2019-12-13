import json


with open('main_list.json', 'r') as file:
    assingments = json.load(file)


def show_assignments():
    """ Shows a list of the assignments with a reference number"""
    items = [i for i in assingments[1].keys()]
    for i in items:
        print(f'{items.index(i)}: {i}')

    index = int(input('Enter the number of the finished assignment: '))     # Should do this somewhere else
    return items[index]


def change_state(dict_key):
    """ Changes the state of the assignment to True to indicate that an assignment is done"""
    assingments[1][dict_key][1] = True

    with open('test_list.json', 'w') as file:
        json.dump(assingments, file)


if __name__ == '__main__':
    index = show_assignments()
    change_state(index)

