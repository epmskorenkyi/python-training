"""
Task05 Module
=============

Contains function which takes a comma-separated string and returns a last element
(separated by a last comma) or the entire string if there is no comma in it.
"""


def last_element(string):
    """
    Takes a comma-separated string and returns a last element (separated by a
    last comma) or the entire string if there is no comma in it

    Arguments:
        string - comma separated string
    """
    parse = str(string).split(',')
    return parse[len(parse) - 1]

print last_element('string without comma')
print last_element('first,second,third,last')