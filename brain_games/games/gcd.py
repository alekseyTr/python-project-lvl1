"""Gcd game logic."""

from math import gcd

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_questions():
    """Get questions for game.

    Returns:
        list

    """
    return ['25 50', '100 52', '3 9']


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: str

    Returns:
        int

    """
    question_parts = question.split()
    x, y = int(question_parts[0]), int(question_parts[1])

    return gcd(x, y)
