"""
Task02 module
=============

Words Count
"""


import os, re, collections


info = {'Lines': 0, 'Chars': 0, 'Words': 0}
reg = re.compile(r'\b')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    info['Lines'] += 1
    info['Chars'] += len(line)
    info['Words'] += len(reg.findall(line)) / 2

print info
