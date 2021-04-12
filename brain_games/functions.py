"""Common functions."""

from random import randint


def is_even(number):
    """Validate number.

    Parameters:
        number: int

    Returns:
        bool

    """
    return not number % 2


def is_prime(n):
    """Return True if n is prime.

    Parameters:
        n: int

    Returns:
        bool

    """
    if n in [2, 3]:  # noqa: WPS510
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def generate_random_numbers(count=10):
    """Generate random list of numbers.

    Parameters:
        count: int

    Returns:
        list

    """
    return (x + randint(0, 10) ** randint(1, 5) for x in range(count))
