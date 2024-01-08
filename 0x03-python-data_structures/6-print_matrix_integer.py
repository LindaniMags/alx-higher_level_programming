#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for left in matrix:
        for right in left:
            print("{:d}".format(right), end=" " if right != left[-1] else "")
        print()
