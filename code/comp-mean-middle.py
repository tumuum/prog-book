list1 = eval(input('A list of ints please: '))
list2 = eval(input('Another list of ints please: '))

means =[]

for k in [list1,list2]:
	sum = 0
	for i in k:
		sum = sum + i		

	mean = sum/len(k)
	means.append(mean)
	
if means[0] == means[1]:
	print('Means match!')
else:
	print('Means do not match!')
