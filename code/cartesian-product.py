first_set=eval(input('Enter a set: '))
second_set=eval(input('Enter another set: '))

product= set()

for x in first_set:
	for y in second_set:
		product.add((x,y))

print(product)
