"""
Task01 module
=============

Write a non-recursive function calculating a factorial of a number using an
xrange function.
"""


def factorial(num):
    """Returns a factorial of an integer.

    :Parameters:
        - num: an integer;

    :Return:
        factorial number

    :Exceptions:
        - ValueError: if a num is less than zero.
        - TypeError: if a num is not an integer.
    """
    if isinstance(num, int):
        if num < 0:
            raise ValueError('Value is less than zero.')
        elif num > 1:
            res = 1
            for n in xrange(2, num + 1):
                res *= n
            return res
        else:
            return 1
    else:
        raise TypeError('Value is not integer.')
