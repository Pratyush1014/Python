class test :
	def __init__(self,name) :
		self.name = name 
		print 'creation of ',self.name
	def __repr__(self) :
		print 'all Objects have been created'
		return str()
	def __del__(self) :
		print self.name,' Object has been destroyed'
def main() :
	obj1 = test('alpha')
	obj2 = test('bravo')
	obj3 = test('Charlie')
	obj4 = test('Delta')
	obj4.__repr__()
	print obj4
	del obj4
	print 'Process ends here'
main()
	
