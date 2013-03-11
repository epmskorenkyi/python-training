"""
Task08 module
=============

Print a number of sentences in a file (a sentence shall and in either a dot .
or a tripple-dot ....
"""

import os, re


input_file = open(os.path.join(os.path.dirname(__file__), 'alice.txt'), 'r')
output_file = open(os.path.join(os.path.dirname(__file__), 'alice08.txt'), 'w')

sentences = re.split(r'(?<!\.)\.(?!\.)|(?<!\.)\.{3}(?!\.)', input_file.read())
output_file.write('Text has %s sentences.\n' % len(sentences))

input_file.close()
output_file.close()
