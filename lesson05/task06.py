"""
Task06 module
=============

Print a number of all occurences of double characters in a file (e.g. ee).
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice06.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

count = 0
search = re.compile(r'(.)\1')
for line in input_file.readlines():
    count += len([match.group() for match in search.finditer(line)])

output_file.write('Found %s doubled characters.\n' % count)

input_file.close()
output_file.close()
