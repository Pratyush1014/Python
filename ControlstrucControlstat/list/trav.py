list = []
i = 0
while True:
	print 'Enter the element you want to enter '
	d = input()
	list.append(d)
	print "Do you want to continue (y/n)"
	ch = raw_input()
	if ch == 'y':
		continue
	else:
		break
print list
for i in range (0,len(list),1) :
	print list[i]
	
