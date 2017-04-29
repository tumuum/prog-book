# Instead of 'alist != []' you can directly put alist after if.
# The empty-list, the empty-string and 0 evaluates to False, otherwise
# lists, strings, integers, floats evaluate to True in the context of 
# boolean operators.

def remove_head(alist):
	"""Removes the first item in a list and returns the resulting list"""
	if alist != []:
		return alist[1:]
	else:
		return alist 
