"""
Task01 module
=============

Transaction Manager
"""


def decorator(f):
    """Transaction decorator"""
    f.counter = 0

    def wrapper(*args):
        f.counter += 1
        print 'Transaction %s for %s started.' % (f.counter, f.__name__)
        try:
            res = f(*args)
            print 'Transaction %s for %s completed' % (f.counter, f.__name__)
            return res
        except:
            print 'Transaction %s for %s cancelled' % (f.counter, f.__name__)

    return wrapper


@decorator
def add(a, b):
    """Adds numbers"""
    return a + b

@decorator
def sub(a, b):
    """Subtract numbers"""
    return a - b

@decorator
def div(a, b):
    """Divide numbers"""
    return float(a) / float(b)

if __name__ == '__main__':
    print add(1, 2)
    print sub(1, 2)
    print div(1, 2)
    print div(1, 0)
    print add(2, 2)
    print add(2, 2)
    print div(1, 4)
