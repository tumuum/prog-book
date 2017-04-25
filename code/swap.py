"""
Two possible solutions.

One alters the list you used in the function call. If you do not
want this behavior; for instance you want to keep your original list while
having a separate swapped version; you need to have the second one.
"""

def swap(alist,index1,index2):

	if index1 + 1 > len(alist) or index2 +1 > len(alist):
		return None
	
	hold = alist[index1]
	alist[index1] = alist[index2]
	alist[index2] = hold
	return alist


def swap2(a_list,first_index,second_index):
	length = len(a_list)

	if first_index > length-1 or second_index > length -1:
		return None

	accum = []

	for x in range(length):
		if x == first_index:
			accum.append(a_list[second_index])
		elif x == second_index:
			accum.append(a_list[first_index])
		else:
			accum.append(a_list[x])

	return accum 
