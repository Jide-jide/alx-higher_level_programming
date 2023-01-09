#!/usr/bin/python3
"""
Returns all available attributes and methods of an object
"""

def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return list(dir(obj))
