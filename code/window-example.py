def check(in_str):
	"""Checks whether the string consists of a's and b's
	without the pattern abab"""

	accept=True  #flag for accept/reject status
	window = ''  #keep track of last 4 symbols

	for c in in_str:
		if c == 'a' or c == 'b':
			#append c to the end of windo
			wwindow += c
			if len(window) > 4:
				#trim the window to 4 syms
				window = window[1:]
		else:
			#reject if any sym not a or b
			accept = False

		if window == 'abab':
			#reject if abab catched
			accept = False

	return accept
