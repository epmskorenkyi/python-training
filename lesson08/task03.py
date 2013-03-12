"""
Task03 module
=============

Context Manager
"""


import contextlib


@contextlib.contextmanager
def transaction(level):
    print 'Start transaction:', level
    try:
        yield
        print 'Success transaction:', level
    except:
        print 'Cancel transaction:', level

def my_func(a, b, c):
    with transaction('root'):
        print a
        with transaction('nested successful'):
            print b
        with transaction('nested with error'):
            print c
            raise Exception

my_func(1, 2, 3)