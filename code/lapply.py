def lapply(f,l):

	retval = []		
	for x in l:
		retval.append(f(x))

	return retval	
