n = input("enter any number: ")
i = 1
c = 0
while i<=n :
	if n%i == 0:
		c+=1
		i+=1
	else :
		i+=1
		continue
if c == 2 :
	print "prime"
else :
	print "not"	
