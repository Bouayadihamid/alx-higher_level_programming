#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
        for num in matrix:
            if len(num) == 0:
                print(0)
            for i in range(len(num)):
                print("{}".format(num), end="\n" if i is len(num) - 1 else " ")
