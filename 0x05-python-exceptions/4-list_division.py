#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

	    """function that divides element by element 2 lists.
    Args:
        my_list_1: list 1
        my_list_2: list 2
        list_length: length of list
    Returns: New list with all the divisions
    """	

	new = []
	for item in range(list_length):
		try:
			result = my_list_1[item] / my_list_2[item]
		except TypeError:
			result = 0
			print("wrong type")
		except ZeroDivisionError:
			result = 0
			print("division by 0")
		except IndexError:
			result = 0
			print("out of range")
		finally:
			new.append(result)
	return new
