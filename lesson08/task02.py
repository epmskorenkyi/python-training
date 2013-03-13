"""
Task01 module
=============

Hello World Decorator
"""


def decorator_wrapper(word):
    """Decorator with parameter"""
    def decorator(func):
        def wrapper(arg):
            func(arg)
            print word
        return wrapper
    return decorator


@decorator_wrapper('World!')
def hello(arg):
    """Prints it's argument"""
    print arg

hello('Hello')
