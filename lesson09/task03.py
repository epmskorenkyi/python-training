"""
Task03 module
=============

Timer
"""


import sys
import signal


def sigint_handler(signum, frame):
    """SIGINT handler"""
    sys.stdout.write('\nUser input cancelled.\n')


def sigalrm_handler(signum, frame):
    """SIGALRM handler"""
    sys.stdout.write('.')


if __name__ == "__main__":
    signal.signal(signal.SIGINT, sigint_handler)
    signal.signal(signal.SIGALRM, sigalrm_handler)

    signal.setitimer(signal.ITIMER_REAL, 1, 1)

    print raw_input()

