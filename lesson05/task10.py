"""
Task10 module
=============

Replace each occurence of Alice was to Alice is and print a number of modified
phrases; sentences breaking though lines shall be modified correctly as well.
"""


import os, re


input_pass = os.path.join(os.path.dirname(__file__), 'alice.txt')
output_pass = os.path.join(os.path.dirname(__file__), 'alice10.txt')
input_file = open(input_pass, 'r')
output_file = open(output_pass, 'w')

replace = re.subn(r'(Alice\s+)was', r'\1is', input_file.read())
output_file.write(replace[0] + 'Modified %s phrases' % replace[1])

input_file.close()
output_file.close()
