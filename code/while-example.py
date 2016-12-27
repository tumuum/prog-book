
n = input('An integer please? ("q" to quit) ')

while n != 'q': 
	n = int(n)

	if n%2 == 0:
		print('You entered an even integer')		
	else:
		print('You entered an odd integer')		
	
	n = input('An integer please? ("q" to quit) ')

print('Bye!')
