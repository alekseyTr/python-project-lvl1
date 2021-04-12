"""Logger for game."""

import prompt


def welcome_and_return_user():
    """Log welcome message and asq user name.

    Returns:
        user: str

    """
    print('Welcome to the Brain Games')
    user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user))
    return user


def question(question_text):
    """Log question."""
    print('Question: {0}'.format(question_text))


def answer(answer_text):
    """Log user answer."""
    print('Your answer: {0}'.format(answer_text))


def incorrect_answer(user_answer, correct_answer, user_name):
    """Log message for incorrect user answer."""
    message = "'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!"  # noqa: E501
    print(message.format(user_answer, correct_answer, user_name))


def correct_result():
    """Log message for correct user answer."""
    print('Correct')


def congratulations(user):
    """Log message for successful end game."""
    print('Congratulations, {0}!'.format(user))


def description(description_text):
    """Log description of the game."""
    print(description_text)
