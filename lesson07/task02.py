"""
Task02 module
=============

Create a function returning a list of all numbers N smaller than input integer M
such that N is a multiplier of 3 while N + 1 is a multiplier of 5. Use it to
print all such numbers smaller than 100.
"""


def multiplier(range_limit):
    """Returns a a list of numbers smaller than given limit such that N is a
    multiplier of 3 while N + 1 is a multiplier of 5.

    :Parameters:
        - range_limit: an integer;

    :Return:
        list of numbers

    :Exceptions:
        - ValueError: if a num is less than zero.
        - TypeError: if a num is not an integer.
    """
    if isinstance(range_limit, int):
        if range_limit < 0:
            raise ValueError('Value is less than zero.')
        else:
            return [res for res in xrange(range_limit)
                    if not res % 3 and not (res + 1) % 5]
    else:
        raise TypeError('Value is not integer.')

print multiplier(100)
