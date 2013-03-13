"""
Task05 module
=============

Flatten
"""


import collections


def flatten(*args):
    """Flattens args iterator

    :Parameters:
        - args: arbitrary numbers of iterable items

    :Exceptions:
        - TypeError: if arg is not an iterable.
    """
    for arg in args:
        if not isinstance(arg, collections.Iterable):
            raise TypeError('Not iterable params')

    items = [iter(arg) for arg in args]
    while len(items):
        to_remove = []
        for item in items:
            try:
                yield item.next()
            except StopIteration:
                to_remove.append(item)
        for rem in to_remove:
            items.remove(rem)

    # return itertools.chain(*[el for el in itertools.izip_longest(*args)])

if __name__ == '__main__':
    for el in flatten((1, 2, 3), (1, 2, 3, 4)):
        print el
