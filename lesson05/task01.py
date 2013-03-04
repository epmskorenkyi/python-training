"""
Task01 module
=============

Remove all empty lines in a file alice.txt and print a number of removed lines.
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice01.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

# for looking hot to use multi line search
# next task will parse not whole text but line by line
data = input_file.read()
empty = len(re.findall(r'^\n', data, re.M))

output_file.write('Removed %s empty lines\n' % empty)
output_file.write(re.sub(r'\n{2,}', '\n', data))

input_file.close()
output_file.close()
