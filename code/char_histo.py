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
	for x in store:
		print(x[0],x[1]*'*')

input = input("Give me a string: ")

count_store = []

for x in input:
	add_char(count_store,x)


draw_histo(count_store)
