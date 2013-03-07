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
    return tuple(string[:10] + string[-10:])

parsed_str = string_trans('012345678909876543210')
print ''.join(parsed_str[:10])
print ''.join(parsed_str[-10:])
print ''.join(parsed_str)

