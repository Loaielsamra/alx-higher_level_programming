#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for r in matrix:
        for i, j in enumerate(r):
            print("{:d}".format(j), end="")
            if (i < len(row) - 1):
                print("{}".format(" "), end="")
        print()
