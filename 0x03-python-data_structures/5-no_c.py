#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
	 """Remove all characters c and C from a string."""
	new_str = my_string.translate({ord(letter): None for letter in 'cC'})
	return (new_str)
