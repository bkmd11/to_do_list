import time
import os
import random

from colorama import Fore, Style

from tools import strings


"""I am a 'fun' message that will play once a week is complete"""


def finished(week):
    """I take a week and figure out if it is the last week, then return a function"""
    if week == strings.LAST_WEEK_STRING:
        finished_class()
    else:
        finished_week()


def finished_week():
    """ Prints a fun message when I finish all assignments"""
    os.system(strings.CLS)
    colors = list(vars(Fore).values())
    count = 0
    while count != 11:
        time.sleep(1)
        print(' ' * random.randint(0, 100), end='')
        print(
            f'{Style.BRIGHT}{random.choice(colors)}Another '
            f'{random.choice(colors)}Week '
            f'{random.choice(colors)}Complete! ', end=''
        )
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} *', end='')
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} **')
        count += 1


def finished_class():
    # Todo: add credit countdown
    """ Prints a fun message when I finish a class"""
    os.system(strings.CLS)
    colors = list(vars(Fore).values())
    count = 0
    while count != 11:
        time.sleep(1)
        print(' ' * random.randint(0, 100), end='')
        print(
            f'{Style.BRIGHT}{random.choice(colors)}  One   '
            f'{random.choice(colors)} Step '
            f'{random.choice(colors)}   Closer! ', end=''
        )
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} *', end='')
        print(' ' * random.randint(0, 100) + f'{random.choice(colors)} **')

        count += 1
