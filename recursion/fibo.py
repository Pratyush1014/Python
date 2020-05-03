n = input ("Enter the limit of your series : ")	
a , b = 0 , 1
def fibo () :
	global n,a,b
	if a < n :
		print a 
		c = a+b
		a,b=b,c
		fibo()
fibo()
	
