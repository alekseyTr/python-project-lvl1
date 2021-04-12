"""Even odd game."""

import prompt
from brain_games import logger

DEFAULT_ROUNDS = 3


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


def play(game, rounds=None):
    """Start game.

    Parameters:
        game: game module
        rounds: int

    """
    user = logger.welcome_and_return_user()
    logger.description(game.DESCRIPTION)
    # TODO: use generator functions
    if rounds is None:
        rounds = DEFAULT_ROUNDS

    for question in game.get_questions(rounds):
        logger.question(question)
        answer = prompt.string()
        logger.answer(answer)
        correct_answer = game.correct_answer(question)

        if not is_valid_answer(answer, correct_answer):
            logger.incorrect_answer(answer, correct_answer, user)
            return
        logger.correct_result()

    logger.congratulations(user)
