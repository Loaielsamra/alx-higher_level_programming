#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = []
    for r in matrix:
        newmatrix.append(list(map(lambda x: x * x, r)))
    return newmatrix
