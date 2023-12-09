#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_mx = []
    for row in matrix:
        row_sqr = [num ** 2 for num in row]
        result_mx.append(row_sqr)
    return result_mx
