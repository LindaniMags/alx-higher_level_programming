#!/usr/bin/python3
def magic_string():
    """Returns a string n times the number of iterations"""
    magic_string.n = getattr(magic_string, 'n', 0) + 1
    return("BestSchool, " * (magic_string.n - 1) + "BestSchool")
