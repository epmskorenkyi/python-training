"""
Task04 module
=============

Print a number of vocal letters in first 100 lines of a file.
"""

import os, re


input_file = open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r')
output_file = open(os.path.join(os.path.dirname(__file__), 'alice04.txt'), 'w')

vocal = 0
regex = re.compile(r'[aeiouy]')
for x in xrange(10):
    vocal += len(regex.findall(input_file.readline()))

output_file.write('Found %s vocals in first 100 lines.\n' % vocal)

input_file.close()
output_file.close()
