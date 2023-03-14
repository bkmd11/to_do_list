import webbrowser

from toDoList import strings
""" I simply launch a browser with the desired tabs open"""


def start_class():
    webbrowser.open_new_tab(strings.GMAIL)
    webbrowser.open_new_tab(strings.DRIVE)
    webbrowser.open(strings.DASHBOARD)

