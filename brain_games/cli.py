"""Cli functions."""

import prompt


def welcome_user():
    """Hello function."""
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))
