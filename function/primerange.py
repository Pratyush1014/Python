def prime (num) :
	c = 0
	for i in range (1,num + 1,1) :
		if num % i == 0 :
			c+=1
	if c == 2 :
		return True
	else :
		return False

def main() :
	while True :
		num = input("Enter any number :")
		for i in range (1,num+1,1) :
			if prime(i) :
				print i,
			else :
				continue
		ch = raw_input("Do you want to continue :")
		if ch == 'yes' :
			continue
		else :
			break
main()
 
