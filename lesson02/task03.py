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


from datetime import datetime, timedelta


class MyNumberPrinter:
    """Provides functions related to given number"""

    # time keys range
    __time_keys = ['s', 'm', 'h', 'd']

    def __init__(self, number):
        """Init class with given number

        :Parameters:
            - number: number for initialization
        """
        self.number = number

    def me(self):
        """Prints a number itself"""
        print self.number

    def factorial(self):
        """Prints factorial of a number itself

        :Exceptions:
            - ValueError: if parameter is less than zero
            - TypeError: if parameter is not integer
        """
        def factorial_loop(num):
            if num > 0:
                return num * factorial_loop(num - 1)
            elif num == 0:
                return 1
            else:
                raise ValueError('Value is less than zero.')

        if isinstance(self.number, int):
            print factorial_loop(self.number)
        else:
            raise TypeError('Value is not integer.')

    def string(self, value):
        """Prints a given string concatenated with itself number times

        :Parameters:
            - value: string to concatenate and print
        """
        print str(value) * self.number

    def update(self, new_value):
        """Updates a number value

        :Parameters:
            - new_value: new number for modifications
        """
        self.number = new_value
        print self.number

    def time_in_past(self, letter):
        """Accepts a one letter string from s, m, h, d range and prints a time
        that is a number of seconds, minutes, hours, or days in the past
        accordingly

        :Parameters:
            - letter: one letter string, a time key flag
        :Exceptions:
            - ValueError: if bad time key
        """
        if letter in self.__time_keys:
            now = datetime.now()

            if letter == 'd':
                days = now - timedelta(days=self.number)
                print 'Time passed in days %s' % \
                      days.strftime('%d %b %Y %H:%M:%S')
                return

            total_hours = self.number * 24 + now.hour
            if letter == 'h':
                print 'Time passed in hours %s' % total_hours
                return

            total_minutes = total_hours * 60 + now.minute
            if letter == 'm':
                print 'Time passed in minutes %s' % total_minutes
                return

            total_seconds = total_minutes * 60 + now.second
            print 'Time passed in seconds %s' % total_seconds
        else:
            raise ValueError('Bad time key. Not in [s, m, h, d] range.')


# show functionality
obj_a = MyNumberPrinter(5)
obj_a.me()
obj_a.factorial()
obj_a.string('test_')
obj_a.update(6)
obj_a.time_in_past('s')
obj_a.time_in_past('m')
obj_a.time_in_past('h')
obj_a.time_in_past('d')

obj_b = MyNumberPrinter(3)
obj_b.me()
obj_b.factorial()
obj_b.string('test_')
obj_b.update(15)
obj_b.time_in_past('s')
obj_b.time_in_past('m')
obj_b.time_in_past('h')
obj_b.time_in_past('d')

MyNumberPrinter.me(obj_a)
MyNumberPrinter.me(obj_b)
MyNumberPrinter.factorial(obj_a)
MyNumberPrinter.factorial(obj_b)
