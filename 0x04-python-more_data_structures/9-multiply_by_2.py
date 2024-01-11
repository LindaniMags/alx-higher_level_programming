#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    times_2 = {}
    for key, value in a_dictionary.items():
        times_2.update({key: (value * 2)})
    return times_2
