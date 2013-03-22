"""
Task01 module
=============

Counter
"""


import time
import threading


def counter(number, pause):
    """Prints numbers from 1 to specified number

    :Parameters:
        - number: max number to print
        - pause: time ti sleep after each print
    """
    for i in xrange(1, number + 1):
        print i
        time.sleep(pause)


def status(refresh):
    """Prints threads count

    :Parameter:
        - refresh: time to sleep after each print
    """
    while True:
        threads = threading.enumerate()
        counters = 0
        for thread in threads:
            if thread.name == 'counter':
                counters += 1

        print 'Total threads: %3s, counters: %3s' % (len(threads), counters)

        if counters:
            time.sleep(refresh)
        else:
            break



if __name__ == '__main__':
    t = threading.Thread(target=counter, args=(5, 1), name='counter')
    t.start()

    t = threading.Thread(target=counter, args=(7, .5), name='counter')
    t.start()

    t = threading.Thread(target=counter, args=(15, 0.1), name='counter')
    t.start()

    t = threading.Thread(target=status, args=(.1,), name='status')
    t.start()




