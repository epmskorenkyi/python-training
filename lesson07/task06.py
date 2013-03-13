"""
Task06 module
=============

Consumer
"""


from task05 import flatten


def line_writer():
    yield
    while True:
        print (yield)

if __name__ == '__main__':
    gen = line_writer()
    gen.next()

    for line in flatten(open('/tmp/test1.txt'), open('/tmp/test2.txt')):
        gen.send(line)
