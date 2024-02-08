#!/usr/bin/python3
"""
 A class MyList that inherits from list.
"""


class MyList(list):
    """MyList subclass"""
    def __init__(self):
        """MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the list, but sorted"""
        print(sorted(self))
