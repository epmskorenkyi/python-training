"""
Task04 Module
=============

Contains function transforms string with the following format::

    pos1_value, pos2_value, pos3_value
    named1=named1_value, named2=named2_value

into tuple of positional and a dictionary of named arguments
"""


def revert_params(string):
    """
    Transforms given string with the following format
    format::

        pos1_value, pos2_value, pos3_value
        named1=named1_value, named2=named2_value

    into tuple of positional and a dictionary of named arguments and prints
    them

    :Parameters:
        - string: string in upper format
    """
    args = named = 'None'
    params = string.split('\n')

    if len(params[0].strip()):
        args = params[0].split(', ')

    if len(params[1].strip()):
        named = {}
        named_string = params[1].split(', ')
        for el in named_string:
            pair = el.split('=')
            named[pair[0]] = pair[1]

    print 'Positional: %s' % args
    print 'Named: %s' % named


revert_params('pos1_value, pos2_value, pos3_value\nnamed1=named1_value, named2=named2_value')
revert_params('pos1_value, pos2_value, pos3_value\n')
revert_params('\nnamed1=named1_value, named2=named2_value')
