#!/usr/bin/python3

def raise_exception():
	"""function that raises a type exception.

	You are not allowed to import any module.
	"""	
	try:
		raise Exception
	except Exception as e:
		print("Exception raised")
