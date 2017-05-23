def compose(f,g):
	def retval(x):
		return f(g(x))
	return retval 
