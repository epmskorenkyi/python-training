"""
Task04 Module
=============

Lists all file names, their permissions, ownership, last modified date in a
specified directory (like an ls -l shell command). If no directory is specified
as the first (and only) command-line argument than a current directory shall be
listed. If more than one argument is passed or the specified directory does not
exist and application shall report to standard error and return an error status
code.
"""


import os, sys, time, errno
from pwd import getpwuid
from time import strftime

if len(sys.argv) > 2:
    raise TypeError('Parameters mismatch.')
if len(sys.argv) == 2:
    dir = sys.argv[1]
    if not os.path.isdir(dir):
        raise ValueError('Bad directory pass')
else:
    dir = os.path.dirname(os.path.realpath(__file__)) + os.sep


for filename in os.listdir(dir):
    info = os.stat(dir + filename)
    print '%s %s %s %s %s %s' % (oct(info.st_mode)[-3:],
                                 getpwuid(info.st_uid).pw_name,
                                 getpwuid(info.st_gid).pw_name,
                                 info.st_size,
                                 strftime("%d %b %Y %H:%M:%S", time.localtime(
                                     info.st_mtime)
                                 ),
                                 filename)
