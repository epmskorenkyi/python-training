"""
Task09 module
=============

Print a number of words in a file (words can be separated by either white space
or any separator (e.g. , or -). Pure integers shall not count but identifiers
consisting of a mix of characters and integers shall count).
"""

import os, re


input_file = open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r')
output_file = open(os.path.join(os.path.dirname(__file__), 'alice09.txt'), 'w')

words = 0
search = re.compile(r'\d*[a-zA-Z]+[a-zA-Z\d]')
for line in input_file.readlines():
    words += len(search.findall(line))

output_file.write('Text has %s words.\n' % words)

input_file.close()
output_file.close()
