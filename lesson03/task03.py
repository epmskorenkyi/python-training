"""
Task03 Module
=============

Contains function that takes arbitrary number of positional and named arguments
and returns a string in the following format::

    pos1_value, pos2_value, pos3_value
    named1=named1_value, named2=named2_value

and uses only str.join and str.format methods
"""


def params_list(*args, **kwargs):
    """
    Takes arbitrary number named arguments and return a string in following
    format::

        pos1_value, pos2_value, pos3_value
        named1=named1_value, named2=named2_value

    Arguments:
        args - arbitrary positional arguments
        kwargs - arbitrary named arguments
    """
    positional = ', '.join(str(value) for value in args)
    named = ", ".join(["%s=%s" % (k, v) for k, v in kwargs.items()])
    return '{}\n{}'.format(positional, named)


print params_list('pos1', 'pos2', 'pos3', n1='n1_val', n2='n2_val', n3=1)