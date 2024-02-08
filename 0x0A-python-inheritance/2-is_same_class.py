#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """a function that returns True if the object is
       exactly an instance of the specified class.

    Args:
        obj (any): Object .
        a_class (type): Class.
    Returns:
        True if the object isexactly an
        instance of the specified class.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
