"""Progression game logic."""

DESCRIPTION = 'What number is missing in the progression?'


def get_questions(count):
    """Get questions for game.

    Parameters:
        count: int

    Returns:
        list

    """
    # TODO: generate questions
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
    # TODO: validate question
    if question == '5 7 9 11 13 .. 17 19 21 23':
        return 15
    elif question == '2 5 8 .. 14 17 20 23 26 29':
        return 11
    elif question == '14 19 24 29 34 39 44 49 54 ..':
        return 59
