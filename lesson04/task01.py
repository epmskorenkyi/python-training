"""
Task01 Module
=============

Writes a string Hello world into a file specified as a command-line argument.
"""


import sys


# get first command line param
dir = sys.argv[1]

file = open(dir, 'w')
file.write('Hello World')
