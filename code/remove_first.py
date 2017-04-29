# Once we remove the first occurrence of the given integer, we're done.
# There are various ways to code this. 

def remove_first1(alist,k):
	"""Removes the first occurrence of k from alist.
	It is not efficient; even it removes one occurrence, it goes
	on processing the input."""

	retval = []
	removed = False	

	for x in alist:
		if x == k and not removed:
			removed = True
		else:
			retval.append(x)	
	
	return retval


# There are different ways to end the computation once you
# removed an occurrence.

# Method 1 (use break):

def remove_first2(alist,k):
	"""Removes the first occurrence of k from alist."""

	retval = []

	for x in range(0,len(alist)):
		# Here we use range instead of iterating the list itself
		# We need the current index to get the rest of the list
		# once one occurrence of k is removed.
		if alist[x] == k:
			retval.extend(alist[x+1:]) # This is where we need the index	
			break                    # 'break' terminates for and while loops
		else:
			retval.append(alist[x])	
	
	return retval
	

# Method 2 (use return):

def remove_first3(alist,k):
	"""Removes the first occurrence of k from alist."""

	retval = []

	for x in range(0,len(alist)):
		# Here we use range instead of iterating the list itself
		# We need the current index, to get the rest of the list
		# once one occurrence of k is removed.
		if alist[x] == k:
			retval.extend(alist[x+1:]) # This is where we need the index	
			return retval			 # a return statement terminates the function
		else:
			retval.append(alist[x])	
	
	return retval
