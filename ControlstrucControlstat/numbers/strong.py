n = input("Enter any number :")
b = n
sum = 0
while n>0 :
	d=1
	a = n%10
	while a>0 :
		d = d*a
		a-=1
	sum = sum + d
	n = n/10
if sum == b :
	print "its a strong number"
else :
	print "not"

