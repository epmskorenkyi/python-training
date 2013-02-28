"""
Task06 Module
=============

Contains function which takes a unicode string and encodes it into a printable
US-ASCII character set.
"""


def unicode_to_ascii(string):
    """Encodes given string into a printable US-ASCII character set

    :Parameters:
        - string: string to encode

    :Return:
        encoded string
    """
    return string.encode('utf-8')

test_str1 = u'a\u3042\xe4asdff'
test_str2 = u'\ua000abcd\u07b4'

print test_str1
print repr(test_str1)
print repr(unicode_to_ascii(test_str1))

print test_str2
print repr(test_str2)
print repr(unicode_to_ascii(test_str2))
