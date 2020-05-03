def fibo () :
	a = 0
	b = 1
	list = []
	while a < 100 :
		yield a
		list.append(a)
		c = a+b
		a,b = b,c
#	for i in list :
#		yield i
def main() :
	fibogen = fibo()
	n = input("Enter the term no you wanna get : ")
	for i in range(n):
		value = fibogen.next()
	print value
main()

