"""
Task05 module
=============

Proxy
"""


class Proxy(object):
    """Proxy class"""
    def __init__(self, object):
        self.__dict__['__counter'] = {}
        self.__dict__['__proxy_object'] = object

    def __getattr__(self, attribute):
        value = getattr(self.__dict__['__proxy_object'], attribute)
        return self.__wrapper(attribute, value) if callable(value) else value

    def __setattr__(self, name, value):
        setattr(self.__dict__['__proxy_object'], name, value)

    def __wrapper(self, name, value):
        self.__dict__['__counter'].setdefault(name, 0)

        def result(*args, **kwargs):
            self.__dict__['__counter'][name] += 1
            return value(*args, **kwargs)

        return result

    def statistics(self):
        for func, times in self.__dict__['__counter'].items():
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
