"""
Task03 module
=============

Timer
"""


import sys
import signal


def signal_handler(signum, frame):
    """Signal handler"""
    if signum == signal.SIGINT:
        sys.stdout.write('\nUser input cancelled.\n')
    elif signum == signal.SIGALRM:
        sys.stdout.write('.')


if __name__ == "__main__":
    for signum in [signal.SIGINT, signal.SIGALRM]:
        signal.signal(signum, signal_handler)

    signal.setitimelr(signal.ITIMER_REAL, 1, 1)

    print raw_input()

