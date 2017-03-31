def reverse(aseq):
	retval = []
	for x in aseq:
		retval = [x] + retval
	if type(aseq) is str:
		return ''.join(retval)
	elif type(aseq) is list:
		return retval

def is_palind(astring):
	return astring == reverse(astring)

usr_in = eval(input('Enter a string: '))

if is_palind(usr_in):
	neg = ' '
else:
	neg = ' NOT '

print('Your string is'+neg+'a palindrome')
