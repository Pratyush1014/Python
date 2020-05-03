def add (*number) :
	sum = 0
	print number ,type(number)
	for i in number :
		sum = sum + i 
	return sum
def main () :
	print add ()
	print add (10,20)
	print add (10,20,30)
	print add (10,20,30,40)
	print add (10,20,30,40,50)
main()	
