#!/usr/bin/env python

"""Progression game."""

from brain_games.engine import play
from brain_games.games import progression


def main():
    """Welcome user and start game."""
    play(progression)


if __name__ == '__main__':
    main()
