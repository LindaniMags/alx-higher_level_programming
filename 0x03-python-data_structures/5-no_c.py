#!/usr/bin/python3
def no_c(my_string):
    str = my_string.translate({ord(letter): None for letter in 'cC'})
    return str
