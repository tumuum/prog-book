m = int(input('A non-negative integer please: '))
n = int(input('Another non-negative integer please: '))

product = 0

while n > 0:
	product += m
	n -= 1

print('Product: ' + str(product))
