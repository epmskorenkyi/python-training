"""
Task06 Module
=============

Contains function which takes a unicode string and encodes it into a printable
US-ASCII character set.
"""


def unicode_to_ascii(string, errors='ignore'):
    """
    Encodes given string into a printable US-ASCII character set

    Arguments:
        string - string to encode
        errors - errors param for encode method (default 'ignore')
    """
    return string.encode('ascii', errors)

print unicode_to_ascii(u'aあäasdff')
print unicode_to_ascii(u'aあäasdff', 'backslashreplace')

print unicode_to_ascii(unichr(40960) + u'abcd' + unichr(1972))
print unicode_to_ascii(unichr(40960) + u'abcd' + unichr(1972), 'replace')