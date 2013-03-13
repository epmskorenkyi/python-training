"""
Task03 module
=============

Remove all leading and trailing white-space from a file and print a number of
modified lines.
"""

import os, re


output_file = open(os.path.join(os.path.dirname(__file__), 'alice03.txt'), 'w')

trailing = 0
reg = re.compile(r'^\s*(.*?)\s*$')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    parsed_line = reg.sub(r'\1\n', line)
    if len(line) > len(parsed_line):
        trailing += 1
    output_file.write(parsed_line)

output_file.write('Found %s lines with trailing whitespaces\n' % trailing)
