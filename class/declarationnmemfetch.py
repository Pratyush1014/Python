class test :
	pass
def main() :
	obj1 = test ()
	obj2 = test ()
	obj3 = test ()
	print id(test)
	print id(obj1)
	print id(obj2)
	print id(obj3)
	print id(obj1.__class__)
	obj1.x = 10
	obj1.y = 20
	obj2.x = 10
	obj2.y = 20
	setattr(obj3,'x',10)
	setattr(obj3,'y',20)
	print obj1.__dict__
	print obj2.__dict__
	print obj3.__dict__
	print test.__dict__
	print obj1.__class__.__dict__
	test.a = 10
	print test.__dict__
	print id(obj1.a),id(test.a)
	obj1.a = 100
	print obj1.__dict__
	print test.__dict__
	print id(obj1.a),id(test.a)
main()
