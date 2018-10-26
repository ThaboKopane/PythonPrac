def ackerman_func(m, n):
	if(m<=0):
		return n+1
	elif(m>0 and n==0):
		return ackerman_func(m-1, 1)
	elif(m>0 and n>0):
		return ackerman_func(m-1, ackerman_func(m, n-1))


print(ackerman_func(5,0))