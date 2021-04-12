"""Gcd game logic."""

from math import gcd
from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_questions(count):
    """Get questions for game.

    Parameters:
        count: int

    Returns:
        list

    """
    questions = []
    while len(questions) < count:
        questions.append('{0} {1}'.format(randint(1, 100), randint(1, 100)))

    return questions


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
