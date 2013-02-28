"""
Task01 Module
=============

This is simple module for first task of Python training second lesson
It prints Hello World and a current time
"""


import time
from time import strftime


print 'Hello World,', strftime('%H:%M:%S', time.localtime(time.time()))
