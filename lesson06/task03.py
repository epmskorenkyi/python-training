"""
Task02 module
=============

Alphabet
"""


import os, re, collections


col = collections.Counter()
reg = re.compile(r'[a-z]')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    for char in reg.findall(line.lower()):
        col[char] += 1

for char, count in sorted(col.items()):
    print char, count
