#!/usr/bin/env python

"""Gcd game."""

from brain_games.engine import play
from brain_games.games import prime


def main():
    """Welcome user and start game."""
    play(prime)


if __name__ == '__main__':
    main()
