"""
Task07 module
=============

Consumer
"""


import os, itertools, sys, re


def revert_lines(file):
    """Revert text lines generator"""
    file.seek(0, os.SEEK_END)
    size = file.tell()

    chunk = 32
    pos = max(size - chunk, 0)
    lines = ['']
    while True:
        file.seek(pos, os.SEEK_SET)
        data = file.read(chunk) + lines[0]

        lines = data.splitlines()
        for i in xrange(len(lines) - 1, 0, -1):
            yield lines[i]

        if pos > 0:
            chunk = pos if pos < chunk else chunk
            pos -= chunk
        else:
            yield lines[0]
            break

with open(sys.argv[1], 'r') as f:
    for line in itertools.islice(revert_lines(f), int(sys.argv[2])):
        print line
