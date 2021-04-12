"""Even odd game."""

import prompt
from brain_games import logger


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

        if not game.is_valid_answer(question, answer):
            logger.incorrect_answer(answer, game.correct_answer(question), user)
            return
        logger.correct_result()

    logger.congratulations(user)
