#!/usr/bin/python3
"""
function that reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """
    with open(filename) as f:
        for line in f:
            print(line.strip())
