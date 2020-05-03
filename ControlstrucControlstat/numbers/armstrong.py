n = input("Enter any number")
b = n
d = n
c = 0
while n>0 :
	c+=1
	n=n/10
sum = 0
while b>0 :
	sum = (b%10)**c+sum
	b = b/10
if d == sum :
	print "its an armstrong number"
else :
	print "not"
	
