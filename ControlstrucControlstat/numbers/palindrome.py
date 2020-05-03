n = input("Enter any number :")
b = n
rev = 0
while n>0 :
	rev =rev*10 +n%10
	n=n/10
if b == rev :
	print "Yup its a palindrome"
else :
	print "Nope"
