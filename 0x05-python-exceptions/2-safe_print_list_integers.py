#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    total = 0
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            total += 1
        except (ValueError, TypeError, IndexError):
            continue
    print()
    return total