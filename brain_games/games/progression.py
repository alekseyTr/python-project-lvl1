"""Progression game logic."""

DESCRIPTION = 'What number is missing in the progression?'


def get_questions():
    """Get questions for game.

    Returns:
        list

    """
    return [
        '5 7 9 11 13 .. 17 19 21 23',
        '2 5 8 .. 14 17 20 23 26 29',
        '14 19 24 29 34 39 44 49 54 ..',
    ]


def correct_answer(question):
    """Get correct answer.

    Parameters:
        question: str

    Returns:
        int


    """
    if question == '5 7 9 11 13 .. 17 19 21 23':
        return 15
    elif question == '2 5 8 .. 14 17 20 23 26 29':
        return 11
    elif question == '14 19 24 29 34 39 44 49 54 ..':
        return 59


def is_valid_answer(question, user_answer):
    """Validate answer.

    Parameters:
        question: str
        user_answer: str

    Returns:
        bool

    """
    return int(user_answer) == correct_answer(question)
