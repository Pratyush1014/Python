n = input("Enter any number :")
i = 1
factors = []
while i<=n :
	if n%i == 0 :
		factors.append(i)
	i+=1
print factors
factors.remove(n)
sum = sum(factors)	
if sum == n :
	print "Perfect num"
else :
	print "Not"
