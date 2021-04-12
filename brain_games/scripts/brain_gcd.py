#!/usr/bin/env python

"""Gcd game."""

from brain_games.engine import play
from brain_games.games import gcd


def main():
    """Welcome user and start game."""
    play(gcd)


if __name__ == '__main__':
    main()
