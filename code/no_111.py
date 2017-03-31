def no_111(word):
	count = 0
	retval = True	

	for s in word:
		if s == '1':
			count = count + 1
		else:
			count = 0

		if count == 3:
			retval = False	
	
	return retval



def no_111_alt(word):
	count = 0
	for s in word:
		if s == '1':
			count = count + 1
		else:
			count = 0
		if count == 3:
			return False

	return True


input_string = input("Enter a string in {0,1}* ('X' for quit): ")

while input_string != 'X':

	if no_111(input_string):
		print('Accept')
	else:
		print('Reject.')

	if no_111_alt(input_string):
		print('Accept')
	else:
		print('Reject.')

	input_string = input("Enter a word ('X' for quit): ")

print('Good-bye!')



