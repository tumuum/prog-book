def occurs_count(lst,obj):
	"""returns the number of times obj occurs in lst"""
	count = 0
	for x in lst:
		if x == obj:
			count += 1
	return count
