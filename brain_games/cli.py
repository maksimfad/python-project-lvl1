"""This is module where welcome_user function defined."""

import prompt


def welcome_user():
    """Use this funciton to get user name and print greeting with it."""
    name = prompt.string('May I have your name? ')
    print('Hello, {0}'.format(name))
