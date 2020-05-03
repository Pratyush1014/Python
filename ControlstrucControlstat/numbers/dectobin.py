n = input("Enter any number :")
bin = 0
i = 0
while n>0 :
	bin = (n%2)*10**i + bin
	i = i+1
	n = n/2
print bin
