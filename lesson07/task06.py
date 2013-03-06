"""
Task06 module
=============

Consumer
"""


import itertools
from task05 import flatten


def text_writter(text):
    """Text writter generator"""
    for line in text.splitlines():
        print line
        yield line

for flat in flatten(text_writter(open('/tmp/test1.txt', 'r').read()),
                    text_writter(open('/tmp/test2.txt', 'r').read())):
    pass