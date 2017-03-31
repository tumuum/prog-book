list1 = eval(input('Give me a list: '))
list2 = eval(input('Give me another list: '))


if len(list1) < len(list2):
	shorter = len(list1)
else:
	shorter = len(list2)

corresps = 0 #number of correspondences

for i in range(shorter):
	if list1[i] == list2[i]:
		corresps = corresps + 1

print('The number of corresponding elements is ' + str(corresps))  
