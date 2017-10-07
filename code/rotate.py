def rotate(s, n):
	while n !=0:
		s = _rotate(s)
		n -= 1
	return s

def _rotate(s):
	return s[1:] + [s[0]]

def rotate2(s, n):
	if n == 0:
		return s 
	else:
		return rotate2(s[1:]+[s[0]],n-1)
