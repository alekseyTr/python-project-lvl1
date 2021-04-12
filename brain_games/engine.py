"""Even odd game."""

import prompt
from brain_games import logger


def is_valid_answer(user_answer, correct_answer):
    """Validate answer.
    There may be several options for correct answers.

    Parameters:
        user_answer: str
        correct_answer: mixed

    Returns:
        bool

    """
    if isinstance(correct_answer, list):
        return user_answer in correct_answer

    return int(user_answer) == correct_answer


def play(game):
    """Start game.

    Parameters:
        game: game module

    """
    user = logger.welcome_and_return_user()
    logger.description(game.DESCRIPTION)

    for question in game.get_questions():
        logger.question(question)
        answer = prompt.string()
        logger.answer(answer)
        correct_answer = game.correct_answer(question)

        if not is_valid_answer(answer, correct_answer):
            logger.incorrect_answer(answer, correct_answer, user)
            return
        logger.correct_result()

    logger.congratulations(user)
