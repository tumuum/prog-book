def reverse_string(astring):
	retval = ''
	for s in astring:
		retval = s + retval
	return retval

def reverse_list(alist):

	retval = []
	for s in alist:
		retval = [s] + retval
	return retval

def reverse(aseq):
	retval = []
	for x in aseq:
		retval = [x] + retval
	if type(aseq) is str:
		return ''.join(retval)
	elif type(aseq) is list:
		return retval

# in using eval for input, you need to 
# provide quotes for strings
usr_input = eval(input('Enter a list or string: ')) 

print('The reverse of your input: ',reverse(usr_input))
