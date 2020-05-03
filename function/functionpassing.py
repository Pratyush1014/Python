def main() :
	x = input("Enter any number  : ")
	def prime (x) :
		c = 0
		for i in range (1,x):
			if x%i == 0 :
				c+=1
			else :
				continue
		if c == 2 :
			return True
		else :
			return False 
	primefactor(prime)
def primefactor (prime):

	if (prime) :
		print 'passed'
	else :
		print 'failed'
main()
