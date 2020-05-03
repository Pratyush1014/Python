n = input("Enter the series limit :")
a = 0
b = 1
c = 0
fibo = []
nonfibo = []
while c<=n:
	i = 0
	bb = b
	c = a+b
	a = b
	b = c
	fibo.append(c)
	while bb+1<c:
		nonfibo.append(bb+1)
		bb+=1
print fibo
print nonfibo
	
