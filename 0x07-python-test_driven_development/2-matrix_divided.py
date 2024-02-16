#!/usr/bin/python3

def matrix_divided(matrix, div):
    counter = 0
    for element in matrix:
        for j in element:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError('matrix must be a matrix (list of lists) of integers / floats')
            counter += 1
    if counter != len(matrix[0]) * len(matrix):
        raise TypeError('Each row of the matrix must have the same size')
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(j / div, 2) for j in element] for element in matrix]
