def prime(n) :
	c=0
	for i in range (1,n+1) :
		if n%i == 0 :
			c+=1
	if c==2 :
		return True 
	else :
		return False
def main() :
	list = [11,23,34,5,34,2,54,67,78,78,56,54,3,3,2,2,34,45,56,7,78,] 	
	print map (prime ,list)
	print filter(prime ,list)
main()

