"""Even odd game."""

import prompt


def is_even(number):
    """Validate number.

    Parameters:
        number: int

    Returns:
        bool

    """
    return not number % 2


def correct_answer(question_number):
    """Get correct answer.

    Parameters:
        question_number: int

    Returns:
        list

    """
    return ['yes', 'y'] if is_even(question_number) else ['no', 'n']


def is_valid_answer(question_number, user_answer):
    """Validate answer.

    Parameters:
        question_number: int
        user_answer: str

    Returns:
        bool

    """
    return user_answer in correct_answer(question_number)


def generate_numbers():
    """Get numbers for game.

    Returns:
        list

    """
    return range(3)


def start_game(user_name):
    """Start game.

    Parameters:
        user_name: str

    """
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for number in generate_numbers():
        print('Question: {0}'.format(number))
        user_answer = prompt.string()
        print('Your answer: {0}'.format(user_answer))

        if not is_valid_answer(number, user_answer):
            print("'{0}' is wrong answer ;(. Correct answer was '{1}'. Let's try again, {2}!".format(user_answer, correct_answer(number), user_name))
            return
        print('Correct!')
    print('Congratulations, {0}!'.format(user_name))
