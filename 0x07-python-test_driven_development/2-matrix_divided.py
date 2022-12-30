#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    
    matrix_len = len(matrix)

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
       
    for i in range(matrix_len):
        if len(matrix[0]) == len(matrix[i]):
            pass
        else:
            raise TypeError("Each row of the matrix must have the same size")

        for j in range(len(matrix[0])):
            if type(matrix[i][j]) in [int, float]:
                pass
            else:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    
    return new_matrix
