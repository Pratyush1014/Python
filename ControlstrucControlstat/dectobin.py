n = input()
s = 0
i=0
while n>0 :
	s = (n%2)*10**i+s
	i += 1
	n = n/2
print s 
