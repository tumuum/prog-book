def seen_before(alist):
	
	seen_elements=[]

	for e in alist:
		if e in seen_elements:
			print(str(e) + ' seen before')
		else:
			print(str(e) + ' new to me')

		seen_elements.append(e)
