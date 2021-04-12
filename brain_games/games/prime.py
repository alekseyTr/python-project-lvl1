"""Prime game logic."""

from brain_games import functions

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_questions(count):
    """Get questions for game.

    Parameters:
        count: int

    Returns:
        list

    """
    return functions.generate_random_numbers(count)


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: str

    Returns:
        list

    """
    return ['yes', 'y'] if functions.is_prime(int(question)) else ['no', 'n']
