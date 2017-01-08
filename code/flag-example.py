def check(in_str):
	"""Checks whether the string consists of a's and b's
	without more than 3 consecutive a's"""

	accept=True #flag for accept/reject status
	a_count = 0 #counter for cons a's

	for c in in_str:
		if c == 'a':
			a_count += 1
		elif c == 'b':
			a_count = 0
		else:
			#reject if any sym not a or b
			accept = False

		if a_count > 3:
			#reject if more than 3 cons a's
			accept = False

	return accept
