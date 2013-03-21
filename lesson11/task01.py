"""
Task01 module
=============

File Copy
"""


import argparse
import sys


parser = argparse.ArgumentParser()

parser.add_argument('positional', nargs='*', help='Input, output files.')

parser.add_argument('-i', '--input', help='Input file')
parser.add_argument('-o', '--output', help='Output file.')

parser.add_argument('-v', '--verbose', help='increase output verbosity',
                    action='store_true')
parser.add_argument('-s', '--buffer-size', default=8196, type=int,
                    help='Buffer size in bytes. Default 8196b.')

args = parser.parse_args()

try:
    pointer = 0
    input_path, output_path = args.input, args.output

    if not input_path:
        input_path = args.positional[pointer]
        pointer += 1

    if not output_path:
        output_path = args.positional[pointer]
        pointer += 1

    if len(args.positional) > pointer:
        parser.error('Too many positional params.')

    input = open(input_path)
    output = open(output_path, 'w')
    while True:
        chunk = input.read(args.buffer_size)
        if chunk:
            output.write(chunk)
            if args.verbose:
                sys.stdout.write('.')
        else:
            sys.stdout.write('\n')
            break
except IndexError:
    parser.error('Too less positional params.')
except IOError, e:
    print e
    sys.exit(1)
except OSError, e:
    print e
    sys.exit(1)








