#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    matrix_cpy = []
    for mat in matrix:
        sqr = list(map(lambda x: x**2, mat))
        matrix_cpy.append(sqr)
    return matrix_cpy
