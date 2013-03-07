"""
Task02 module
=============

Performance
"""


import timeit, string


repeat_count = 1000000

timer = timeit.Timer('t = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)')
print repeat_count, string.rjust('tuples:', 7), timer.timeit(repeat_count)


timer = timeit.Timer('l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]')
print repeat_count, string.rjust('lists:', 7), timer.timeit(repeat_count)

timer = timeit.Timer('s = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}')
print repeat_count, string.rjust('sets:', 7), timer.timeit(repeat_count)


