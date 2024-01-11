#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    ordered_keys = list(a_dictionary.ordered_keys())
    ordered_keys.sort()
    for key in ordered_keys:
        print("{}: {}".format(key, a_dictionary[key]))
