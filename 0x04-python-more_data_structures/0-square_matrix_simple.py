#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in range(0, len(matrix)):
        new_matrix.append(list(map(lambda x: x * x, matrix[row])))

    return new_matrix
