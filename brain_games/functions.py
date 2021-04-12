"""Common functions."""


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
