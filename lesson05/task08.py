"""
Task08 module
=============

Print a number of sentences in a file (a sentence shall and in either a dot .
or a tripple-dot ....
"""

import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice08.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

output_file.write('Text has %s sentences.\n' %
                  len(re.split('\.{3}|\.', input_file.read())))

input_file.close()
output_file.close()
