n = input("Enter any number :")
i = 1
primefactors=[]
while i<=n :
	d = 1
	c = 0
	if n%i ==0 :
		while d<=i :
			if i%d == 0 :
				c+=1
			d+=1
		if c == 2:
			primefactors.append(i)	
	i+=1
print primefactors		
