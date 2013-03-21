"""
Task02 module
=============

Regexp
"""


import argparse
import re


class ActionsList(argparse.Action):
    """Puts arbitrary command line args and puts them into a list"""
    def __call__(self, parser, namespace, values, option_string=None):
        if hasattr(namespace, 'actions_order'):
            namespace.actions_order += [option_string,]
        else:
            namespace.actions_order = [option_string,]


class ActionExecute(object):
    """Executes specific action by key"""
    def __init__(self, file):
        """Init

        :Parameters:
            - file: file with text
        """
        self.file = file

    def call_by_key(self, key):
        """Runs specific task by key value

        :Parameters:
            - key: actions key
        """
        count = 0
        self.file.seek(0)

        if key == '-e':
            reg = re.compile(r'^\n$')
            for line in self.file:
                if reg.match(line):
                    count += 1

            print 'File contains %s empty lines.' % count
        elif key == '-b':
            regex = re.compile(r'^\s+\n')
            for line in self.file:
                if regex.match(line):
                    count += 1

            print 'File contains %s blank lines.' % count
        elif key == '-W':
            reg = re.compile(r'^\s*(.*?)\s*$')
            for line in self.file:
                parsed_line = reg.sub(r'\1\n', line)
                if len(line) > len(parsed_line):
                    count += 1

            print 'File contains %s lines with trailing whitespaces.' % count
        elif key == '-v':
            regex = re.compile(r'[aeiouy]')
            for x in xrange(100):
                count += len(regex.findall(self.file.readline()))

            print 'File contains %s vocals in first 100 lines.' % count
        elif key == '-n':
            regex = re.compile(r'\d+')
            for line in self.file.readlines():
                count += len(regex.findall(line))

            print 'File contains %s numbers.' % count
        elif key == '-d':
            search = re.compile(r'(.)\1')
            for line in self.file.readlines():
                count += len(search.findall(line))

            print 'File contains %s doubled characters.' % count
        elif key == '-D':
            search = re.compile(r'(?:^|(?<=(.)))(?!\1)(.)\2(?!\2)')
            for line in self.file.readlines():
                count += len([match.group() for match in search.finditer(line)])

            print 'File contains %s exactly doubled characters.' % count
        elif key == '-s':
            count = re.split(r'\b\.?\.\.?(?=\s)', self.file.read())
            print 'File contains %s sentences.' % len(count)
        elif key == '-w':
            search = re.compile(r'\d*[a-zA-Z]+[a-zA-Z\d]')
            for line in self.file.readlines():
                count += len(search.findall(line))

            print 'File contains %s words.' % count
        elif key == '-t':
            count = re.subn(r'(Alice\s+)was', r'\1is', self.file.read())
            print 'File contains %s time phrases.' % count[1]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='File path.', type=argparse.FileType())

    parser.add_argument('-e', action=ActionsList, nargs=0, help='Empty.')
    parser.add_argument('-b', action=ActionsList, nargs=0, help='Blank.')
    parser.add_argument('-W', action=ActionsList, nargs=0, help='White.')
    parser.add_argument('-v', action=ActionsList, nargs=0, help='Vocals.')
    parser.add_argument('-n', action=ActionsList, nargs=0, help='Numbers.')
    parser.add_argument('-d', action=ActionsList, nargs=0, help='Doubles.')
    parser.add_argument('-D', action=ActionsList, nargs=0,
                        help='Advanced doubles.')
    parser.add_argument('-s', action=ActionsList, nargs=0, help='Sentence.')
    parser.add_argument('-w', action=ActionsList, nargs=0, help='Words.')
    parser.add_argument('-t', action=ActionsList, nargs=0, help='Time.')

    args = parser.parse_args()


    if __name__ == '__main__':
        t = ActionExecute(args.file)
        if hasattr(args, 'actions_order'):
            for key in args.actions_order:
                t.call_by_key(key)

