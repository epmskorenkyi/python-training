"""
Task01 module
=============

Exceptions
"""


import os
import sys


if __name__ == '__main__':
    # data
    input_path = '/tmp/test01.txt'
    output_path = '/tmp/test2.txt'

    try:
        file_a = open(input_path, 'r')

        file_b = os.open(output_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        os.write(file_b, file_a.read())

        sys.stdout.write('All operations successfully completed.\n')
    except IOError, e:
        sys.stderr.write('%s file error: %s.\n' % (e.filename, e.strerror))
        sys.exit(1)
    except OSError, e:
        sys.stderr.write('%s file error: %s.\n' % (e.filename, e.strerror))
        sys.exit(1)

