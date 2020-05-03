list = []
i = 0
temp = 0
while True :
        n = input("Enter the elements to be pushed")
        list.append(n)
        ch = raw_input("Do you wanna continue (y/n)")
        if ch == 'y' :
                continue
        else :
                break
print list
max = 0
min = list[0]
for i in range (0,len(list),1) :
	if max < list[i] :
		max = list[i]
	if min > list[i] :
		min = list[i]
print "max is :",max
print "min is :",min
