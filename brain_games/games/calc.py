"""Even odd game."""

DESCRIPTION = 'What is the result of the expression?'


def get_questions():
    """Get questions for game.

    Returns:
        list

    """
    return ['55 + 10', '25 - 11', '25 * 7']


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

