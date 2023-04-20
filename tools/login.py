import pyperclip

import passwords
"""I copy a password to the clipboard"""


def clipboard():
    pyperclip.copy(passwords.password)
