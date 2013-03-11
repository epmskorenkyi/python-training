"""
Task02 module
=============

Replace all blank lines (lines consisting of just a white space) and print a
number of modified lines. Empty lines shall not count.
"""

import os, re


output_file = open(os.path.join(os.path.dirname(__file__), 'alice02.txt'), 'w')

blank = 0
regex = re.compile(r'^\s+\n')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    if regex.match(line):
        blank += 1
        output_file.write('\n')
    else:
        output_file.write(line)

output_file.write('Removed %s blank lines\n' % blank)
output_file.close()
