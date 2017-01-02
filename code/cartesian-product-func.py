def product(A,B):
	"""Takes two sets A and B, and returns their 
	cartesian product as a set of 2-tuples."""

	product = set()
	for x in A:
		for y in B:
			product.add((x,y))

	"""Now it is time to return the result"""

	return product
