"""
Task06 Module
=============

Contains function which takes a string and replaces all vocal letters in it to
an uppercase using a str.replace method.
"""


def vocal_to_upper(string):
    """
    Takes a string and replaces all vocal letters in it to an uppercase

    Arguments:
        string - string to modification
    """
    for char in ['a', 'e', 'i', 'j', 'o', 'u', 'y']:
        string = string.replace(char, char.upper())
    return string

print vocal_to_upper('All vocal letters are big!')