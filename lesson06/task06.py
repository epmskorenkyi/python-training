"""
Task02 module
=============

Words Usage
"""


import os, re, collections, sys


col = collections.Counter()
reg = re.compile(r'[a-zA-Z0-9]+')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    for word in reg.findall(line.lower()):
        col[word] += 1

print col.most_common(int(sys.argv[1]))
