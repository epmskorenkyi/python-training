"""
Task04 module
=============

Print a number of vocal letters in first 100 lines of a file.
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice04.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

vocal = 0
for x in xrange(100):
    vocal += len(re.findall(r'[aeiouy]', input_file.next()))

output_file.write('Found %s vocals in first 100 lines.\n' % vocal)

input_file.close()
output_file.close()
