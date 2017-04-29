def remove_all(alist,k):
	"""Removes all occurrences of k from alist."""

	retval = []

	for x in alist:
		if x != k:
			retval.append(x)	

	return retval
	
