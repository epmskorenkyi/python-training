"""
Task03 module
=============

Remove all leading and trailing white-space from a file and print a number of
modified lines.
"""

import os, re


output_file = open(os.path.join(os.path.dirname(__file__), 'alice03.txt'), 'w')

trailing = 0
match = re.compile(r'^\s+[^\s]|[^\s]\s+\n')
replace = re.compile(r'^\s*(.+[^\s])\s*\n')
for line in open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r'):
    if match.match(line):
        trailing += 1
        line = replace.sub(r'\1\n', line)
    output_file.write(line)

output_file.write('Found %s lines with trailing whitespaces\n' % trailing)
output_file.close()
