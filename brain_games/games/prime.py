"""Prime game logic."""

from brain_games.functions import is_prime

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_questions():
    """Get questions for game.

    Returns:
        list

    """
    return ['7', '8', '156']


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: str

    Returns:
        list

    """
    return ['yes', 'y'] if is_prime(int(question)) else ['no', 'n']


def is_valid_answer(question, user_answer):
    """Validate answer.

    Parameters:
        question: str
        user_answer: str

    Returns:
        bool

    """
    return user_answer in correct_answer(question)
