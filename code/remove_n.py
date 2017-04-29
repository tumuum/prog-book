def remove_n(alist,k,n):
	"""Removes the first n occurrences of k from alist."""

	if n <= 0:
		return alist

	retval = []

	for x in range(0,len(alist)):
		# Here we use range instead of iterating the list itself
		# We need the current index, to get the rest of the list
		# once one occurrence of k is removed.
		if alist[x] == k:
			if n == 1:
				retval.extend(alist[x+1:]) # This is where we need the index	
				return retval			 # a return statement terminates the function
			else:
				n = n-1	
		else:
			retval.append(alist[x])	
	
	return retval
