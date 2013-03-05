"""
Task05 Module
=============

Contains function which takes a comma-separated string and returns a last element
(separated by a last comma) or the entire string if there is no comma in it.
"""


def last_element(string):
    """Takes a comma-separated string and returns a last element (separated by a
    last comma) or the entire string if there is no comma in it

    :Parameters:
        - string: comma separated string

    :Return:
        result string
    """
    return string.rsplit(',', 1)[-1]

print last_element('string without comma')
print last_element('first,second,third,last')
