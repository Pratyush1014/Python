list = [1,2,3,4,5,6,7,8,9]
s = input("Enter element to search :")
x = len (list)
l = 0
h = x-1
i = 0
while l<=h :
	m = (l+h)/2
	if list[m] == s :
		print "search is found"
		break
	elif list[m]>s :
		h = m
	else :
		l = m
