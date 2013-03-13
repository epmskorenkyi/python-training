"""
Task05 module
=============

Print a number of numbers in a file; each number shall count only once (e.g.
1234 shall count only once, not 4 times).
"""

import os, re


input_file = open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r')
output_file = open(os.path.join(os.path.dirname(__file__), 'alice05.txt'), 'w')

numbers = 0
regex = re.compile(r'\d+')
for line in input_file.readlines():
    numbers += len(regex.findall(line))

output_file.write('Found %s numbers.\n' % numbers)

