class test :
	a = 10
	@classmethod
	def method(cls) :
		print "address of class is :",id(cls)
		str = raw_input("Enter a text to display");
		print str
def main():
	print 'memory of test class : ',test.__dict__
	#creating an object of test class
	object = test()
	print 'memory of object : ',object.__dict__
	#calling of method
	print 'called by obj'
	object.method()
	print 'called by class'
	test.method()
	print test.a
	print object.a
	print object.__class__.a
main()
	
