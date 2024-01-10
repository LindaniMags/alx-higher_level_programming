#!/usr/bin/python3

def uniq_add(my_list=[]):
    list_1 = []
    result = 0
    for val in my_list:
        if val not in list_1:
            result += val
            list_1.append(val)
    return result
