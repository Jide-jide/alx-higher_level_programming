#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
	i = len(my_list) - 1
	
	if len(my_list) > 0:
		while i != -1:
			print("{:d}".format(my_list[i])
			i -= 1
	else:
		return my_list[0]

