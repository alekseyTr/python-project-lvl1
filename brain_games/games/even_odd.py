"""Even odd game logic."""

from brain_games import functions

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


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
        question: int

    Returns:
        list

    """
    return ['yes', 'y'] if functions.is_even(question) else ['no', 'n']
