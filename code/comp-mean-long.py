list1 = eval(input('A list of ints please: '))
list2 = eval(input('Another list of ints please: '))

sum1 = 0
for i in list1:
	sum1 = sum1 + i		

mean1 = sum1/len(list1)

sum2 = 0
for i in list2:
	sum2 = sum2 + i		

mean2 = sum2/len(list2)

if mean1 == mean2:
	print('Means match!')
else:
	print('Means do not match!')
