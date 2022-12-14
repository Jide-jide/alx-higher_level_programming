#!/usr/bin/python3
"""Defines a function that divides all elements of a matrix.

Attributes:
    matrix_divided: divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    
    """Divides all elements of a matrix.
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): Value to divide by.
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix isn't of the same size.
        TypeError: If an element of any list is not an integer or float.
        TypeError: If a row in the matrix is not a list.
        TypeError: If div is not an integer or a float.
        ZeroDivisionError: If div is equal to 0.
    Returns:
        matrix: A result of the division.
    """
   
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if matrix == None or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
     
    matrix_len = len(matrix)
    
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
