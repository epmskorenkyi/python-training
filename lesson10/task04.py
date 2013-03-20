"""
Task04 module
=============

Custom Dictionary
"""


def dict_with_attrs(*attrs):
    """Returns extended dictionary class"""
    class Dic(dict):
        """Exteneded dictionary"""
        __slots__ = attrs

        def __init__(self, *args, **kwargs):
            super(Dic, self).__init__(*args)
            for name, value in kwargs.iteritems():
                setattr(self, name, value)

    return Dic

if __name__ == '__main__':
    klass = dict_with_attrs('test', 'second')
    d = klass({'s': 1}, test=10)
    d.second = 11
    d[2] = 3

    print d.test
    print d.second
    # d.other = 3
