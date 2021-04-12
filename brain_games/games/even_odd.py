"""Even odd game logic."""

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
