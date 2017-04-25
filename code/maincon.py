def maincon(a_formula):
	
	open = 0

	for x in a_formula:
		if x == '(':
			open = open + 1
		elif x == ')':
			open = open - 1
		elif x in ['-','V','A','>'] and open == 1:
			return x
