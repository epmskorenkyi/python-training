"""
Task06 Module
=============

Contains function which takes a string and returns the first 10 characters off
it concatenated with the last 10 characters.
"""


def string_cutter(string):
    """Takes a string and returns the first 10 characters off it concatenated
    with the last 10 characters

    :Parameters:
        string - string for modification

    :Return:
        changed string
    """
    return string[:10] + string[-10:]

print string_cutter('short')
print string_cutter('1234567890 this will be cut 0987654321')
print string_cutter('1234567890987654321')

