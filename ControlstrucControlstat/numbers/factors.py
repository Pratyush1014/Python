n = input("Enter any number :")
i = 1
factors = []
while i<=n :
	if n%i == 0 :
		factors.append(i)
		i+=1
	else :
		i+=1
		continue
print factors
if len(factors) == 2 :
	print "prime number"
