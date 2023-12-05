#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for num in matrix:
            if len(num) == 0:
                print()
            for i in range(len(num)):
                print("{:d}".format(num[i]), end="\n" if i is len(num) - 1 else " ")
