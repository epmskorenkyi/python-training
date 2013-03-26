"""
Task03 module
=============

Producer-Consumers
"""


import argparse
import os
import multiprocessing
import time
import threading
import Queue


def worker(queue):
    """Writes lines from queue which starts from capital letter into output file

    :Parameters:
        = queue: queue of text lines
    """
    output = os.open(output_path, os.O_APPEND | os.O_WRONLY)
    while True:
        line = queue.get()
        if line[0].isupper():
            os.write(output, line)
        queue.task_done()


if __name__ == '__main__':
    input_path = os.path.join(os.path.dirname(__file__), 'alice.txt')
    output_path = os.path.join(os.path.dirname(__file__), 'output.txt')

    parser = argparse.ArgumentParser()
    child_type = parser.add_mutually_exclusive_group(required=True)
    child_type.add_argument('-t', action='store_true', help='Use threads.')
    child_type.add_argument('-p', action='store_true', help='Use processes.')
    args = parser.parse_args()

    start = time.time()

    if args.t:
        queue = Queue.Queue()

        for i in xrange(10):
            t = threading.Thread(target=worker, args=(queue,))
            t.daemon = True
            t.start()
    elif args.p:
        queue = multiprocessing.JoinableQueue()

        for i in xrange(10):
            p = multiprocessing.Process(target=worker, args=(queue,))
            p.daemon = True
            p.start()

    for line in open(input_path):
        queue.put(line)

    queue.join()

    print time.time() - start






