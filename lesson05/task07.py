"""
Task07 module
=============

The same task as above but tripples shall not count (e.g. eee shall not count).
"""

import os, re


input_file = open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r')
output_file = open(os.path.join(os.path.dirname(__file__), 'alice07.txt'), 'w')

count = 0
search = re.compile(r'(?:^|(?<=(.)))(?!\1)(.)\2(?!\2)')
for line in input_file.readlines():
    count += len([match.group() for match in search.finditer(line)])

output_file.write('Found %s doubled characters.\n' % count)

input_file.close()
output_file.close()
