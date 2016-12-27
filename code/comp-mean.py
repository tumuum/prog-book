def mean(k):
	sum = 0
	for i in k:
		sum = sum +i
	return sum/len(k)

list1 = eval(input('A list of ints please: '))
list2 = eval(input('Another list of ints please: '))
	
if mean(list1) == mean(list2):
	print('Means match!')
else:
	print('Means do not match!')
