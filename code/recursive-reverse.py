def reverse(seq):
	if not seq:
		return seq
	else:
		return reverse(seq[1:]) + [seq[0]]
