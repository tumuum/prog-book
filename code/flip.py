input_string = input('Enter a string: ')

accu = ''

for c in input_string:	
	if c.isupper():
		accu = accu +  c.lower()
	elif c.islower():
		accu = accu + c.upper()
	else:
		accu = accu + c

print(accu)
