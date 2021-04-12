"""Even odd game."""

from brain_games.functions import is_even

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_questions():
    """Get questions for game.

    Returns:
        list

    """
    return range(3)


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: int

    Returns:
        list

    """
    return ['yes', 'y'] if is_even(question) else ['no', 'n']


def is_valid_answer(question, user_answer):
    """Validate answer.

    Parameters:
        question: int
        user_answer: str

    Returns:
        bool

    """
    return user_answer in correct_answer(question)
