list = []
i = 0
temp = 0
while True :
	n = input("Enter the elements to be pushed")
	list.append(n)
	ch = raw_input("Do you eanna continue (y/n)")
	if ch == 'y' :
		continue
	else :
		break
print list
for i in range (0,len(list),2) :
	if i == len(list) - 1 :
		break
	temp = list[i]
	list[i] = list[i+1]
	list[i+1] = temp
print list


