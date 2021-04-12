"""Logger for game."""

import prompt


def welcome_and_return_user():
    print('Welcome to the Brain Games')
    user = prompt.string('May I have your name? ')
    print('Hello, {0}!'.format(user))
    return user


def question(question):
    print('Question: {0}'.format(question))


def answer(answer):
    print('Your answer: {0}'.format(answer))


def incorrect_answer(user_answer, correct_answer, user_name):
    message = "'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!"
    print(message.format(user_answer, correct_answer, user_name))


def correct_result():
    print('Correct')


def congratulations(user):
    print('Congratulations, {0}!'.format(user))


def description(description):
    print(description)
