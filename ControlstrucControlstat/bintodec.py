n = input()
s = 0
while n>0 :
	s = (n%10)*2+s*2
	n = n/10
print s
