"""
In this problem, we need a structure to store which character occurs how many
times. It is best to use a dict object; but here we will use only lists. We will
keep counts in a list of two element lists. For example: 

[["a",3],["b",5],["z",3]] 

"""

def add_char(store,char):
	"""add a character to the count store"""	
	already_there = False

	for x in store:
		if x[0] == char:
			x[1] = x[1] + 1
			already_there = True

	if not already_there:
		store.append([char,1])


def draw_histo(store):
	
	# Frist we find the maximum frequency

	max_freq = 1
	for x in store:
		if x[1] > max_freq:
			max_freq = x[1]

	# Then we modify our store such that
	# every count is replaced by max_freq - count

	for x in store:
		x[1] = max_freq - x[1]

	# Then we start drawing from top
	# We put a "* " for each char with a zero
	# count, and two space  characters for counts
	# greater than zero; and we decrement those
	# counts. (extra space is for a better look)
	# We need to do this for max_freq times; for this
	# purpose we use a while loop
	

	count = max_freq

	while count > 0:
		
		line = ""
		for x in store:
			if x[1] == 0:
				line = line + "* " 
			else:
				line = line + "  "
				x[1] = x[1] -1

		print(line)
		count = count-1

	# Finally we print the characters
	chars_line = ""
	for x in store:
		chars_line = chars_line + x[0] + " "
	print(chars_line)	



input = input("Give me a string: ")

count_store = []

for x in input:
	add_char(count_store,x)

draw_histo(count_store)
