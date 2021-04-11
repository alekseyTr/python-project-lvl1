#!/usr/bin/env python

"""Even Odd game."""

import prompt
from brain_games.games.calc import start_game


def main():
    """Welcome user and start game."""
    print('Welcome to the Brain Games')
    name = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(name))

    start_game(name)


if __name__ == '__main__':
    main()
