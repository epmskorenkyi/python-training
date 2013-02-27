"""
Task03 Module
=============

This is simple module for third task of Python training second lesson
It contains a class **MyNumberPrinter** which accepts a number in a constructor
and has the following instance methods:

- **me**: prints a number itself;
- **factorial**: prints a factorial of a number;
- **string**: prints a string concatenated with itself number times;
- **update**: modifies a number value and prints a new value;
- **time_in_past**: accepts a one letter string that is either of s, m, h, d and
print a time that is a number of seconds, minutes, hours, or days in the past
accordingly;

A module also creates several MyNumberPrinter instances for showing its
functionality.
"""
from datetime import datetime


class MyNumberPrinter:
    """**MyNumberPrinter** class

    Provides functions related to given number
    """

    # time keys range
    __time_keys = ["s", "m", "h", "d"]

    def __init__(self, number):
        """
        Init class with given number

        Arguments:
            number - number for initialization
        """
        self.n = number

    def me(self):
        """
        Prints a number
        """
        print self.n

    def factorial(self):
        """
        Prints factorial of a number

        Throws:
            ValueError exception
        """
        def factorial_loop(n):
            """
            Returns factorial of a given number

            Throws:
                ValueError exception

            Arguments:
                n - integer number for factorial
            """
            if n > 0:
                return n * factorial_loop(n - 1)
            elif n == 0:
                return 1
            else:
                raise ValueError("Value is less than zero.")

        if isinstance(self.n, int):
            print factorial_loop(self.n)
        else:
            raise ValueError("value is not integer.")

    def string(self, value):
        """
        Prints a given string concatenated with itself number times

        Arguments:
            value - string to concatenate and print
        """
        res = ""
        for i in range(self.n):
            res += value
        print res

    def update(self, new_value):
        """
        Updates a number value

        Arguments:
            new_value - new number for modifications
        """
        self.n = new_value
        print self.n

    def time_in_past(self, letter):
        """
        Accepts a one letter string from s, m, h, d range and prints a time
        that is a number of seconds, minutes, hours, or days in the past
        accordingly

        Throws:
            ValueError exception

        Arguments:
            letter - one letter string, a time key flag
        """
        if letter in self.__time_keys:
            now = datetime.now()

            if letter == "d":
                print "Time passed in days %s" % self.n
                return

            total_hours = self.n * 24 + now.hour
            if letter == "h":
                print "Time passed in hours %s" % total_hours
                return

            total_minutes = total_hours * 60 + now.minute
            if letter == "m":
                print "Time passed in minutes %s" % total_minutes
                return

            total_seconds = total_minutes * 60 + now.second
            print "Time passed in seconds %s" % total_seconds
        else:
            raise ValueError("Bad time key. Not in [s, m, h, d] range.")


# show functionality
obj_a = MyNumberPrinter(5)
obj_a.me()
obj_a.factorial()
obj_a.string("test_")
obj_a.update(6)
obj_a.time_in_past("s")
obj_a.time_in_past("m")
obj_a.time_in_past("h")
obj_a.time_in_past("d")

obj_b = MyNumberPrinter(3)
obj_b.me()
obj_b.factorial()
obj_b.string("test_")
obj_b.update(15)
obj_b.time_in_past("s")
obj_b.time_in_past("m")
obj_b.time_in_past("h")
obj_b.time_in_past("d")

MyNumberPrinter.me(obj_a)
MyNumberPrinter.me(obj_b)
MyNumberPrinter.factorial(obj_a)
MyNumberPrinter.factorial(obj_b)
