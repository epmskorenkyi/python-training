"""
Task02 module
=============

Fork
"""


import argparse
import os


def loop_fork(times):
    print 'pid %s started' % os.getpid()

    if times > 1:
        child_pid = os.fork()

        if child_pid:
            print 'pid %s spawned %s' % (os.getpid(), child_pid)
            os.waitpid(child_pid, 0)
            print 'pid %s completed' % os.getpid()
        else:
            loop_fork(times - 1)
    else:
        print 'pid %s completed' % os.getpid()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('depth', type=int, help='Max recursion depth.')
    args = parser.parse_args()

    loop_fork(args.depth)
