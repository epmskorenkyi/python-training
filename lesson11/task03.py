"""
Task03 module
=============

Phone book
"""


import argparse
import os
import sys
import re


class PhoneBook(object):
    """Contacts manager"""
    def __init__(self, store_path):
        """Init method
        :Parameters:
            - store_path: path to book file
        """
        self.store_path = store_path

    def add_contact(self, first_name, last_name, phone_numbers=[]):
        """Adds new contact. Print message if contact already exists.

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name
            - phone_numbers: list of contact numbers

        """
        if self.__search_contact(first_name, last_name):
            print >> sys.stdout, 'Contact already exists:'
        else:
            book = open(self.store_path, 'a+')
            book.write('First Name: %s; Last Name: %s; Phone Numbers: %s\n' %
                       (first_name, last_name, ', '.join(phone_numbers)))

    def search_contacts(self, first_name, last_name):
        """Search and prints contacts by first or last names.

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name
        """
        contacts = []

        first_name = first_name if first_name else ''
        last_name = last_name if last_name else ''

        reg = re.compile(r'[First Name: (.*' + first_name + '.*?); '
                         'Last Name: (.*' + last_name + '.*?);]')
        for line in open(self.store_path):
            if reg.match(line):
                contacts.append(line)

        if contacts:
            for contact in contacts:
                print >> sys.stdout, contact
        else:
            print >> sys.stdout, 'Contacts not found'

    def delete_contact(self, first_name, last_name):
        """Deletes contact. Prints message if contact does not exists.

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name
        """
        search_for = 'First Name: %s; Last Name: %s;' % (first_name, last_name)
        if not self.__rewrite(search_for, full_match=False):
            print >> sys.stdout, 'Contact not exists.'

    def __read_all(self):
        """Returns tuple of all contacts"""
        contacts = []
        for line in open(self.store_path):
            contacts.append(line)
        return contacts

    def print_contacts(self, limit=False, order=False):
        """Prints all contacts.

        :Parameters:
            - limit: count limit
            - order: sort contacts

        """
        contacts = []

        if order:
            contacts = sorted(self.__read_all())
            if limit:
                contacts = contacts[:limit + 1]
        else:
            if limit:
                book = open(self.store_path)
                for i in xrange(limit + 1):
                    contacts.append(book.readline())
            else:
                contacts = self.__read_all()

        for contact in contacts:
            print >> sys.stdout, contact

    def print_contact(self, first_name, last_name):
        """Print given by first and last name contact

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name
        """
        res = self.__search_contact(first_name, last_name)
        if res:
            print >> sys.stdout, res
        else:
            print >> sys.stdout, 'Contact not found.'

    def edit_contact(self, first_name, last_name, new_first_name=False,
                     new_last_name=False, new_number=False, del_number=False,
                     edit_number=False):
        """Edits contact. Prints message if contact was not found.

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name
            - new_first_name: new first name to set
            - new_last_name: new last name to set
            - new_number: new number to add
            - del_number: number to delete
            - edit_number: number, new number tuple

        """
        contact = edited_contact = self.__search_contact(first_name, last_name)

        if contact:
            if new_first_name:
                edited_contact = re.sub(r'(First Name: ).*?(;)',
                                        r'\1' + new_first_name + r'\2',
                                        edited_contact)
            if new_last_name:
                edited_contact = re.sub(r'(Last Name: ).*?(;)',
                                        r'\1' + new_last_name + r'\2',
                                        edited_contact)
            if new_number:
                edited_contact = edited_contact[:-1] + ', ' + new_number + '\n'
            if del_number:
                edited_contact = re.sub(r', ' + del_number, '', edited_contact)
            if edit_number:
                edited_contact = re.sub(r'' + edit_number[0], edit_number[1],
                                        edited_contact)

            self.__rewrite(contact, edited_contact)
        else:
            print >> sys.stdout, 'Contact not found.'

    def __search_contact(self, first_name, last_name):
        """Search contact by first and last names

        :Parameters:
            - first_name: contact first name
            - last_name: contact last name

        :Return:
            contact or False if not found
        """
        search_for = 'First Name: %s; Last Name: %s;' % (first_name, last_name)
        for line in open(self.store_path):
            if search_for in line:
                return line
        return False

    def __rewrite(self, old_line, new_line=False, full_match=True):
        """Rewrites contacts or delete it if not specified

        :Parameters:
            - old_line: contact to modify
            - new_line: contact to set, if False - only remove
            - full_match: check part or full line match
        :Return:
            operation result: True or False
        """
        temp = open(self.store_path + '.tmp', 'w')
        res = False
        for line in open(self.store_path):
            if (full_match and old_line == line) or (not full_match
                                                     and old_line in line):
                res = True
                if new_line:
                    temp.write(new_line)
            else:
                temp.write(line)

        if res:
            os.rename(self.store_path + '.tmp', self.store_path)
            pass
        else:
            os.remove(self.store_path + '.tmp')
            pass

        return  res



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    # main commands group
    commands = parser.add_mutually_exclusive_group(required=True)
    commands.add_argument('-a', '--add', action='store_true',
                          help='Add new contact')
    commands.add_argument('-d', '--delete', action='store_true',
                          help='Delete contact')
    commands.add_argument('-p', '--print-contacts', action='store_true',
                        help='Print N contacts')
    commands.add_argument('-e', '--edit', action='store_true',
                          help='Edit given contacts')
    commands.add_argument('-s', '--search', action='store_true',
                          help='Edit given contacts')

    # additional params
    parser.add_argument('-f', '--first-name', help='Contact first name.')
    parser.add_argument('-l', '--last-name', help='Contact last name.')
    parser.add_argument('-n', '--number', default=False, type=int,
                        help='Number of contacts to print.')
    parser.add_argument('-o', '--order', action='store_true',
                        help='Number of contacts to print.')
    parser.add_argument('-P', '--phone-numbers', nargs='+', default=[],
                        help='List of phone numbers.')

    # edit actions params
    parser.add_argument('--set-first-name', help='Contact new first name.')
    parser.add_argument('--set-last-name', help='Contact new last name.')
    parser.add_argument('--add-number', help='Contact new number.')
    parser.add_argument('--del-number', help='Contact number to delete.')
    parser.add_argument('--edit-number', nargs=2,
                        help='Contact number to edit.')

    args = parser.parse_args()

    book = PhoneBook('/tmp/phone_book.txt')

    if args.add:
        if args.first_name and args.last_name:
            book.add_contact(args.first_name, args.last_name,
                             args.phone_numbers)
        else:
            parser.error('Not enough data for creating contact. '
                         'Please enter first and last names.')
    if args.delete:
        if args.first_name and args.last_name:
            book.delete_contact(args.first_name, args.last_name)
        else:
            parser.error('Not enough data for deleting contact. '
                         'Please enter first and last names.')

    if args.print_contacts:
        if args.first_name and args.last_name:
            book.print_contact(args.first_name, args.last_name)
        elif args.first_name or args.last_name:
            parser.error('Not enough data for printing contact. '
                         'Please enter first and last names.')
        else:
            book.print_contacts(args.number, args.order)

    if args.search:
        if args.first_name or args.last_name:
            book.search_contacts(args.first_name, args.last_name)
        else:
            parser.error('Not enough data for searching contact. '
                         'Please enter first or last name.')

    if args.edit:
        if args.first_name and args.last_name:
            func_args = {}
            if args.set_first_name:
                func_args['new_first_name'] = args.set_first_name
            if args.set_last_name:
                func_args['new_last_name'] = args.set_last_name
            if args.add_number:
                func_args['new_number'] = args.add_number
            if args.del_number:
                func_args['del_number'] = args.del_number
            if args.edit_number:
                func_args['edit_number'] = args.edit_number

            if func_args:
                book.edit_contact(args.first_name, args.last_name, **func_args)
            else:
                parser.error('Not specified edit value. Please choose at least'
                             'one of edit field.')
        else:
            parser.error('Not enough data for editing contact. '
                         'Please enter first and last names.')



