"""
Task02 module
=============

Unique Words
"""


import os, re

reg = re.compile(r'[a-zA-Z0-9]+')
unique = set()
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    unique.update(reg.findall(line.lower()))

print 'Unique Words: %s' % len(len(unique))

