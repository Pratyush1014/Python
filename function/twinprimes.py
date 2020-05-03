def prime (num) :
	c = 0
	for i in range(1,num +1,1) :
		if num % i == 0 :
			c+=1
		else :
			continue
	if c == 2 :
		return True
	else :
		return False
#def twin (num1,num2) :
#	if num2 - num1 == 2 :
#		return True
#	else :
#		return False
def main() :
	num = input("Enter the upper limit of your search :")
	for i in range (1,num+1,1) :
		if prime(i) and prime(i+2) :
			print '(',i,i+2,')',
main()	
