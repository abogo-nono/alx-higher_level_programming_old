#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in range(len(matrix)):
        cols = []
        for j in range(len(matrix[i])):
            cols.append(matrix[i][j] * matrix[i][j])
        result.append(cols)
    return result
