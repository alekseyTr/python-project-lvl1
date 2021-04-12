"""Calculator game logic."""

from random import randint

DESCRIPTION = 'What is the result of the expression?'

operands = ['+', '-', '*']


def get_questions(count):
    """Get questions for game.

    Question format: 'a + b', 'a - b'

    Parameters:
        count: int

    Returns:
        list

    """
    questions = []
    while len(questions) < count:
        a, b = randint(1, 100), randint(1, 100)
        if a < b:
            a, b = b, a
        questions.append('{0} {1} {2}'.format(a, operands[randint(0, 2)], b))

    return questions


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
