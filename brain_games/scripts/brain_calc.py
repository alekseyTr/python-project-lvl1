#!/usr/bin/env python

"""Calculator game."""

from brain_games.engine import play
from brain_games.games import calc


def main():
    """Welcome user and start game."""
    play(calc)


if __name__ == '__main__':
    main()
