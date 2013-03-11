"""
Task01 module
=============

Remove all empty lines in a file alice.txt and print a number of removed lines.
"""

import os, re


output_file = open(os.path.join(os.path.dirname(__file__), 'alice01.txt'), 'w')

empty_count = 0
reg = re.compile(r'^\n$')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    if reg.match(line):
        empty_count += 1
    else:
        output_file.write(line)

output_file.write('Removed %s empty lines\n' % empty_count)
output_file.close()
