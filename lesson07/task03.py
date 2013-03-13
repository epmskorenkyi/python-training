"""
Task03 module
=============

Write a generator which produces an infinite sequence of Fibonacci numbers.
Use it to print first 100 Fibonacci numbers followed by every tenth such number
between 100th and 1000th (e.g. 100th, 110th, 120th and so on).
"""


import itertools, string


def fibonacci():
    """Fibonacci numbers generator"""
    a = b = 1
    while True:
        yield a
        a, b = b, a + b

# first 99
for num, value in enumerate(itertools.islice(fibonacci(), 99)):
    print '%4d' % (num + 1), ':', value

# from 100 to 1000 with interval 10
for num, value in enumerate(itertools.islice(fibonacci(), 99, 1000, 10)):
    print '%4d' % (100 + num * 10), ':', value



