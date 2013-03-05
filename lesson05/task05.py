"""
Task05 module
=============

Print a number of numbers in a file; each number shall count only once (e.g.
1234 shall count only once, not 4 times).
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice05.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

numbers = []
regex = re.compile(r'[0-9]+')
for line in input_file.readlines():
    numbers = list(set(numbers + regex.findall(line)))

output_file.write('Found %s numbers.\n' % len(numbers))

input_file.close()
output_file.close()
