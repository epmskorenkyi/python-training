"""
Task05 Module
=============

Prints some statistics about itself to standard output: a path to executable,
command line arguments, imported module names and corresponding file paths,
environment variables.
"""


import os, sys, types, datetime
from time import strftime


print len(sys.modules.items())
print sys.modules.items()
print 'Path to executable: %s' % sys.executable
print 'Command line arguments: % s' % sys.argv

print 'Imported modules (%s):' % len(sys.modules.items())
for module in sys.modules.items():
    print module

print 'Environment variables (%s):' % len(os.environ.items())
for key, val in os.environ.items():
    print key, ': ', val

