"""Even odd game."""

import prompt


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: str

    Returns:
        int

    """
    question_parts = question.split()
    operator = question_parts[1]
    x, y = int(question_parts[0]), int(question_parts[2])

    if operator == '+':
        return x + y
    elif operator == '-':
        return x - y
    elif operator == '*':
        return x * y
    elif operator == '/':
        # todo: деление на ноль
        return x / y


def is_valid_answer(question, user_answer):
    """Validate answer.

    Parameters:
        question: str
        user_answer: str

    Returns:
        bool

    """
    return int(user_answer) == correct_answer(question)


def get_questions():
    """Get numbers for game.

    Returns:
        list

    """
    return ['55 + 10', '25 - 11', '25 * 7']


def start_game(user_name):
    """Start game.

    Parameters:
        user_name: str

    """
    print('What is the result of the expression?')
    for question in get_questions():
        print('Question: {0}'.format(question))
        user_answer = prompt.string()
        print('Your answer: {0}'.format(user_answer))

        if not is_valid_answer(question, user_answer):
            error_message = "'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!"
            print(error_message.format(user_answer, correct_answer(question), user_name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(user_name))
