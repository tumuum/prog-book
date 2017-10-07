def reverse(seq, store=[]):
	if not seq:
		return store 
	else:
		return reverse(seq[1:], [seq[0]] + store)
