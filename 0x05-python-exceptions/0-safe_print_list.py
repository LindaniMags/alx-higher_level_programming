#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    total = 0
    try:
        for el in range(x):
            print(my_list[el], end="")
            total += 1
    except IndexError:
        pass
    print()
    return total
