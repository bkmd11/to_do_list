#! python3
"""takes input and makes a .txt file.
Using this to plan my week for classes.
"""


# Takes input for what needs to get done
def taskManager():
    tasks = {}
    while True:
        chores = input('What assignments are due this week?\n')
        if chores == '':
            break
        dueDate = input('When is this due?\n')
        tasks[chores] = dueDate
    return tasks


# Takes that input and puts it into a dict      
def makeList(dict_):
    count = 1
    mainString = ''
    for k,v in dict_.items():
        string = '{}: {}\n   - {}\n'.format(count,k,v)
        count += 1
        mainString += string
    return str(mainString)


#takes input for list
week_number = input('What week is this?\n')

if week_number == '8':
    week_number = 'THE LAST FUCKING WEEK OF THIS SHITTY SHIT!!!'

else:
    week_number = f'WEEK {week_number}'
    
assignments = taskManager()
mainList = makeList(assignments)

#makes a numbered list and saves it to a file
myList=open('C:\\Users\\Brian Kendall\\Desktop\\School Assignments.txt', 'w')
myList.write(f'ASSIGNMENTS DUE FOR {week_number}:\n\n')
myList.write(mainList)


myList.close()




