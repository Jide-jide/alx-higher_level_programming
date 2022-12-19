#!/usr/bin/python3
def safe_print_integer(value):
	"""
		prints an integer
		Returns True if value has been correctly printed
		You have to use try: / except
		Args:
			value: integer
			Returns True else False
	"""
	try:
		print("{:d}".format(value))
		return True
	except (ValueError, TypeError):
		return False
	print()
