def fun (name=None,age=None) :
	print 'hi ',name,' your ','age is ',age
def main() :
	fun ('alpha',23)	#required arguments
	fun ('alpha')	#default
	fun (age=23)	#keyword as argument
	fun (age = 23,name = 'alpha')
main()

