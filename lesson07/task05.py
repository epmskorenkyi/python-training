"""
Task05 module
=============

Flatten
"""


import itertools, collections


def flatten(*args):
    """Flattens args iterator

    :Parameters:
        - args: arbitrary numbers of iterable items

    :Exceptions:
        - TypeError: if arg is not an iterable.
    """
    for arg in args:
        if not isinstance(arg, collections.Iterable):
            raise TypeError('Not iterable params')

    return itertools.izip_longest(*args)

