"""
Task02 module
=============

Replace all blank lines (lines consisting of just a white space) and print a
number of modified lines. Empty lines shall not count.
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice02.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

blank = 0
regex = re.compile(r'^(?=[^\n])\s+\n')
for line in input_file.readlines():
    if regex.match(line):
        blank += 1
    else:
        output_file.write(line)

output_file.write('Removed %s blank lines\n' % blank)

input_file.close()
output_file.close()