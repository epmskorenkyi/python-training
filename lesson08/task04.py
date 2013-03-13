"""
Task04 module
=============

Method Generator
"""


import functools


def template(self, a, b, c):
    """Template method for class methods"""
    print self.x, a, b, c

method_table = {
    'test': dict(a=10, c=20, b=11),
    'other_test': dict(b=30),
}


def template_methods(template, method_table):
    """Decorator, adds given methods to class"""
    def wrapper(obj):
        for method, params in method_table.items():
            setattr(obj, method, functools.partial(template, obj, **params))
        return obj
    return wrapper


@template_methods(template, method_table)
class A(object):
    """Simple class for showing how decorator works"""
    x = 10
    pass

if __name__ == '__main__':
    a = A
    a.test(b=10)
    a.other_test(a=1, c=5)


