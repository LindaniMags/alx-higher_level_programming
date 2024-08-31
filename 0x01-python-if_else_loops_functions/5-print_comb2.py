#!/usr/bin/python3
"""prints numbers from 0 to 99."""

for num in range(0, 99):
    print('{:02d}, '.format(num), end='')
print('99')
