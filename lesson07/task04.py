"""
Task04 module
=============

Itertools
"""


import itertools


def iter_loop(num1, num2, num3):
    return itertools.izip(
        itertools.repeat(num1),
        itertools.count(num2, num1),
        itertools.chain(
            (num1,),
            itertools.islice(itertools.cycle(
                itertools.chain(xrange(num1 + 1, num3 + 1),
                                xrange(num3 - 1, num1 - 1, -1))),
                2 * (num3 - num1) * num2)),
    )

for pairs in iter_loop(1, 2, 3):
    print pairs





