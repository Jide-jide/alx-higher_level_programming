#!/usr/bin/python3
"""Defines a function add_integer(a, b=98) that adds two integers.

Attributes:
	add_integer: function that adds two integers.
"""

def add_integer(a, b=98):
	"""Adds two integer and/or float values.
    	Args:
        	a (int): First value
        	b (int, optional): Second value. Defaults to 98.
    	Raises:
        	TypeError: If a and b are not integers or floats.
    	Returns:
        	int: Sum of a and b.
	"""

	try:
		assert type(a) in (float, int)
	except:
		raise TypeError("a must be an integer")
	try:
		assert type(b) in (float, int)
	except: 
		raise TypeError("b must be an integer")
		
	a = int(a)
	b = int(b)

	return a + b
