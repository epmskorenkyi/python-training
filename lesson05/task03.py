"""
Task03 module
=============

Remove all leading and trailing white-space from a file and print a number of
modified lines.
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice03.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

trailing = 0
for line in input_file.readlines():
    if re.match(r'^(?=[^\n])\s+|(?=[^\n])\s+$', line):
        trailing += 1
        line = re.sub(r'^(?=[^\n])\s+|(?=[^\n])\s+$', '', line)
    output_file.write(line)

output_file.write('Found %s lines with trailing whitespaces\n' % trailing)

input_file.close()
output_file.close()
