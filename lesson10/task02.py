"""
Task02 module
=============

Truth Table
"""


class TruthTable(object):
    """Mixin class with overridden bool()"""
    def __nonzero__(self):
        if hasattr(self, '__true_values__'):
            return self in self.__true_values__
        elif hasattr(self, '__false_values__'):
            return self not in self.__false_values__
        else:
            raise TypeError('TruthTable: parent class has no truth table.')


class TrueTest(TruthTable, int):
    """Class with truth table including True values"""
    __true_values__ = (0, 1, 2, 3)


class FalseTest(TruthTable, str):
    """Class with truth table including False values"""
    __false_values__ = ('false', 'no')


if __name__ == '__main__':
    print bool(TrueTest(0))
    print bool(TrueTest(4))
    print bool(FalseTest(''))
    print bool(FalseTest('no'))
