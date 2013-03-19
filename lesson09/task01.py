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
    output_path = '/tmp/test02.txt'

    try:
        file_a = open(input_path, 'r')

        file_b = os.open(output_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        for line in file_a:
            os.write(file_b, line)

        sys.stdout.write('All operations successfully completed.\n')
    except IOError, e:
        print >> sys.stderr, e
        sys.exit(1)
    except OSError, e:
        print >> sys.stderr, e
        sys.exit(1)

