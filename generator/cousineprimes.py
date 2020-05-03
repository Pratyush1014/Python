def prime (num) :
	counter = 0
	for i in range (1,num+1,1) :
		if num % i == 0 :
			counter += 1
	if counter == 2 :
		return True
	else :
		return False
def generate (limit) :
	for i in range(1,limit+1,1) :
		if (prime(i)) :
			yield i
def main() :
	limit = input("Enter limit of your search : ")
	term = input("Enter the term you want to search : ")
	ch = generate(limit)
	for i in range(1,term+1,1) :
		c = ch.next()
	print c
main()
