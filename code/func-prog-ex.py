#On the top part of the program, you have your function definition

def starts_with_cap(word):
	if word[0].isupper():
		return True
	else:
		return False

#The interpreter starts to execute your program from here on.
#It consults the definition of the function starts_with_cap
#when it is needed.

input_string = input("Enter a word ('X' for quit): ")

while input_string != 'X':

	if starts_with_cap(input_string):
		print('Starts with a capital letter.')
	else:
		print('Does not start with a capital letter.')

	input_string = input("Enter a word ('X' for quit): ")

print('Good-bye!')
