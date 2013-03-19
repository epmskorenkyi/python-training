"""
Task03 module
=============

Memento
"""


import contextlib
import time
import sys


class Memento:
    """Context manager class"""
    def __init__(self, object, attribute, value):
        self.object = object
        self.attribute = attribute
        self.value = value

    def __enter__(self):
        self.origin_value = getattr(self.object, self.attribute)
        setattr(self.object, self.attribute, self.value)
        return self.object

    def __exit__(self, exc_type, exc_val, exc_tb):
        setattr(self.object, self.attribute, self.origin_value)


@contextlib.contextmanager
def memento(object, attribute, value):
    """Content manager function"""
    origin_value = getattr(object, attribute)
    setattr(object, attribute, value)
    yield
    setattr(object, attribute, origin_value)


if __name__ == '__main__':
    check_time = time.time()
    with Memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        print sys.exit(1)
    print "%.10f" % (time.time() - check_time)

    check_time = time.time()
    with memento(sys, 'exit', lambda x: 'Did you want to exit?'):
        print sys.exit(1)
    print "%.10f" % (time.time() - check_time)



