"""
Task06 Module
=============

Updates a current date and time in a file's first line (stored in the first 50
characters). A file shall be specified as a first argument. Other file content
than first 50 characters shall not be modified.
"""


import time, sys
from time import strftime

if len(sys.argv) > 1:
    file = open(sys.argv[1], 'r+')
    time_str = strftime('%d %b %Y %H:%M:%S', time.localtime(time.time()))
    file.write(time_str.ljust(50))
    file.close()
