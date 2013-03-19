"""
Task04 module
=============

Custom Dictionary
"""


def dict_with_attrs(attrs):
    class Dic(dict):
        __slots__ = attrs

    return Dic

if __name__ == '__main__':
    d = dict_with_attrs('test')()

    d[2] = 3
    d.test = 'test'
    d.other = 3
