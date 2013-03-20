"""
Task05 module
=============

Proxy
"""


import collections


class Proxy(object):
    """Proxy class"""
    counter = None
    proxy_object = None

    def __init__(self, object):
        self.__dict__['counter'] = {}
        self.__dict__['proxy_object'] = object

    def __getattr__(self, attribute):
        value = getattr(self.proxy_object, attribute)
        if isinstance(value, collections.Callable):
            return self.wrapper(attribute, value)

        return value

    def __setattr__(self, key, value):
        setattr(self.proxy_object, key, value)

    def wrapper(self, name, value):
        def result(*args, **kwargs):
            if name in self.counter:
                self.counter[name] += 1
            else:
                self.counter[name] = 1
            return value(*args, **kwargs)

        return result

    def statistics(self):
        for func, times in self.counter.items():
            print '%10s: %s' % (func, times)


class A(object):
    """Test class"""
    phrase = 'Test'

    def test(self):
        print self.phrase

    def param_test(self, param):
            print param


if __name__ == '__main__':
    proxy = Proxy(A())
    # print proxy.phrase
    type(proxy.test)
    proxy.test()
    proxy.test()

    proxy.param_test('wefwf')

    proxy1 = Proxy(A())
    # print proxy.phrase
    type(proxy1.test)
    proxy1.test()
    proxy1.test()

    proxy1.param_test('wefwf')

    proxy.test()

    proxy.statistics()
    proxy1.statistics()
