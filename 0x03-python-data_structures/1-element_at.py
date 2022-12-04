#!/usr/bin/python3
# 1-element_at.py

def element_at(my_list, idx):
	"""Retrieve an element from alist."""
	n = len(my_list)
	if idx < 0:
		return None
	elif idx >= n:
		return None
	else:
		return (my_list[idx])
