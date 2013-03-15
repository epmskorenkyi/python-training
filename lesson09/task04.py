"""
Task04 module
=============

Signals
"""


import atexit
import sys
import signal
from time import sleep


statistics = {'reset_signals': 0, 'total_resets': 0, 'current_signals': 0}

@atexit.register
def full_statistics():
    """Shows total statistics before program ends"""
    total = statistics['reset_signals'] + statistics['current_signals']
    sys.stdout.write('Total signals: %s\n' % total)
    sys.stdout.write('Total resets : %s\n' % statistics['total_resets'])


def signal_handler(signum, frame):
    """Signal handler"""
    if signum == signal.SIGHUP:
        statistics['reset_signals'] += statistics['current_signals']
        statistics['current_signals'] = 0
        statistics['total_resets'] += 1
    elif signum in [signal.SIGTERM, signal.SIGINT]:
        sys.exit(0)
    else:
        statistics['current_signals'] += 1

if __name__ == "__main__":
    diff = [9, 19, 32, 33]
    for signum in [num for num in xrange(1, signal.NSIG) if not num in diff]:
            signal.signal(signum, signal_handler)

    while True:
        sleep(60)
        sys.stdout.write('Signals: %s\n' % statistics['current_signals'])
