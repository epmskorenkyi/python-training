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


def factorial(i):
    """**factorial** function

    Prints factorial of given number

    Throws:
        *ValueError* exception

    Arguments:
        *i* - integer number for factorial
    """
    def factorial_loop(n):
        """**factorial_loop** function

        Returns factorial of given number

        Throws:
            *ValueError* exception

        Arguments:
            *n* - integer number for factorial
        """
        if n > 0:
            return n * factorial_loop(n - 1)
        elif n == 0:
            return 1
        else:
            raise ValueError("Value is less than zero.")

    if isinstance(i, int):
        print factorial_loop(i)
    else:
        raise ValueError("value is not integer.")


def my_args(*args):
    """**my_args** function

    Prints all given arguments

    Arguments:
        *args* - arbitrary number of arguments

    """
    print "my_args params: %s" % str(args)


def harmony(*args):
    """**harmony** function

    Prints harmonic medium value of given arguments

    Arguments:
        *args* - arbitrary number of arguments

    """
    print "Harmonic medium value of %s is %s" % \
          (str(args), sum(args) / len(args))


# functions calls
factorial(0)
factorial(5)

my_args(1,2,3,4)
my_args("First", "Second", "Third")

harmony(2, 2.0)
harmony(2, 2.0, 5.67, 3.02, -1)