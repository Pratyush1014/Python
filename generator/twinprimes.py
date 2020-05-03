def prime (x) :
	c=0
	for i in range (1,x+1) :
		if x%i == 0 :
			c+=1
	if c==2 :
		return True
	else :
		return False	
def twinprime () :
	for i in range (1,1000) :
		if prime(i) and prime(i+2) :
			yield i
		i+=1
while True :
	genobj = twinprime()
	n = input("Enter the term no : ")
	for i in range(n) :
		tp = genobj.next()
	print tp
	ch = input("do you wanna continue 1/2 ")
	if ch == 1 :
		continue
	else :
		break

			
