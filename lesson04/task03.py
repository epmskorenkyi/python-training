"""
Task03 Module
=============

Redirects its standard input into a standard output line by line (like a shell
pipe operator).
"""


import sys


for line in iter(sys.stdin.readline, ''):
    sys.stdout.write(line)

