def n_of_moves(n):
	if n == 1:
		return 1
	else:
		return 2 * n_of_moves(n-1) + 1
