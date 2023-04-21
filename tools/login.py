import time
import pyperclip

from tools import passwords
"""I copy a password to the clipboard"""


def clipboard():
    pyperclip.copy(passwords.PASSWORD)
    print('Password copied!')
    time.sleep(1)
