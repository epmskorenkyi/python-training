"""
Task04 module
=============

Signals
"""


import atexit
import sys
import signal
import os
from time import sleep


statistics = {
    'total_signals': 0,
    'total_resets': 0,
    'current_signals': 0
}

@atexit.register
def full_statistics():
    """Shows total statistics before program ends"""
    print >> sys.stdout, 'Total signals: %s\n' % statistics['total_signals']
    print >> sys.stdout, 'Total resets : %s\n' % statistics['total_resets']


def signal_handler(signum, frame):
    """Signal handler"""
    statistics['total_signals'] += 1
    statistics['current_signals'] += 1

    if signum == signal.SIGHUP:
        statistics['current_signals'] = 0
        statistics['total_resets'] += 1
    elif signum in [signal.SIGTERM, signal.SIGINT]:
        sys.exit(0)

if __name__ == "__main__":
    try:
        for signum in xrange(1, signal.NSIG):
            signal.signal(signum, signal_handler)
    except RuntimeError, e:
        pass

    while True:
        sleep(60)
        sys.stdout.write('Signals: %s\n' % statistics['current_signals'])
