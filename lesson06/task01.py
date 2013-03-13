"""
Task01 module
=============

Packing and unpacking
"""


def string_trans(string):
    """Returns tuple of first and last 10 chars of given string

    :Parameters:
        - string: given string to parse

    :Return:
        a tuple
    """
    return string[:10], string[-10:]

res = string_trans('012345678909876543210')
print res[0]
print res[1]
print res[0] + res[1]
