def moves(n,x,y,z):
	if n == 1:
		print('Move '+str(x)+' to '+str(y))
	else:
		moves(n-1,x,z,y)
		print('Move '+str(x)+' to '+str(y))
		moves(n-1,z,y,x)
