
#for
def mapply_f(f,k,n):
	retval = k
	for x in range(0,n):
		retval = f(retval)	
	return retval

#while
def mapply_w(f,k,n):
	retval = k
	while n != 0:
		retval = f(retval)	
		n -= 1 
	return retval

#recursive
def mapply(f,k,n):
	if n == 0:
		return k
	else:
		return mapply(f,f(k),n-1)
