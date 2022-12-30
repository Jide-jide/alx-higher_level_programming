#!/usr/bin/python3
"""Defines a function that prints a square with the character #.
Attributes:
    print_square: function that prints a square with the character #.
"""


def print_square(size):
    """Prints a square with the character #.
    Args:
        size (int): Size of the square (1 side).
    Raises:
        TypeError: If size is not an integer and less than 0.
        ValueError: If size is less than 0.
    """

    if type(size) == int:
        pass
    else:
        raise TypeError("size must be an integer")
    
    if size >= 0:
        pass
    else:
        raise ValueError("size must be >= 0")
    
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
