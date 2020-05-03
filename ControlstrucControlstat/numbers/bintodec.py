n = input("Enter a binary num :")
dec = 0
i = 0
while n>0 :
	dec = (n%10)*2**i + dec
	n=n/10
	i+=1
print dec
