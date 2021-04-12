#!/usr/bin/env python

"""Even Odd game."""

from brain_games.engine import play
from brain_games.games import even_odd


def main():
    """Welcome user and start game."""
    play(even_odd)


if __name__ == '__main__':
    main()
