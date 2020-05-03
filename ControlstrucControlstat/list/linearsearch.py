from time import sleep
list = [1,2,3,4,5,6,7,8,9]
search = input("Enter number to search :")
i=0
for i in range(0,len(list),1) :
		print list[i]
		sleep (1)
		if search == list[i] :
			print "search found "
			break	
		
