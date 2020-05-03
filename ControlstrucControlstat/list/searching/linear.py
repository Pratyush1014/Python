from time import sleep
list = [1,2,3,4,5,6,7,8,9]
s = input("Enter the value you want to search :")
for data in list :
	print data
	if data == s :
		print "search is found"
		break
	sleep(1)
else :
	print "Search not found"
