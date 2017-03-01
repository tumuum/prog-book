def fibonacci(n):
	
	if n < 0:
		return -1 #error code 
	elif n in [0,1,2,3]:
		return n
	else:
		return fib(2,3,n)

def fib(x,y,k):
	if k == 3:
		return y
	else:
		return fib(y,x+y,k-1)
