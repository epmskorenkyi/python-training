"""
Task02 Module
=============

This is simple module for second task of Python training second lesson
It contains next function:

- **factorial**: accepts one integer and prints its factorial (recursive);
- **my_args**: accepts an arbitrary number of arguments and prints them all;
- **harmony**: takes an arbitrary number of floats and prints their
harmonic medium value;

A module also calls its functions with some arguments.
"""


def factorial(num):
    """Prints a factorial of an integer.

    :Parameters:
        - num: an integer;

    :Return:
        None

    :Exceptions:
        - ValueError: if a num is less than zero.
        - TypeError: if a num is not an integer.
    """
    def factorial_loop(num):
        if num > 0:
            return num * factorial_loop(num - 1)
        elif num == 0:
            return 1
        else:
            raise ValueError('Value is less than zero.')

    if isinstance(num, int):
        print factorial_loop(num)
    else:
        raise TypeError('Value is not integer.')


def my_args(*args, **kwargs):
    """Prints all given arguments

    :Parameters:
        - args: position arguments;
        - kwargs: named arguments

    :Return:
        None
    """
    print 'my_args params:\nposition: %s\nnamed: %s' % (str(args), kwargs)


def harmony(*args):
    """Prints harmonic medium value of given arguments

    :Parameters:
        - args: arbitrary number of arguments

    :Return:
        None

    :Exceptions:
        - TypeError: if parameter is not a number
    """
    denominator = 0
    for value in args:
        try:
            value = float(value)
        except ValueError:
            raise TypeError('Params is not a number')

        if value == 0:
            print 0
            return

        denominator += 1 / value

    print 'Harmonic medium value of %s is %s' % \
          (str(args), len(args) / denominator)


# functions calls
factorial(0)
factorial(5)

my_args(1, 2, 3, 4, n1=11, n2=22, n3=33)
my_args('First', 'Second', 'Third', n1=11, n2=22, n3=33)

harmony(1, 2, 4)
harmony(2, 2.0, 5.67, 3.02, -1)
