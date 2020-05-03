class test :
	x = 10 
def main () :
	obj = test()
	print id(obj) , obj.__dict__ , obj.__class__.__dict__
	print  obj.__class__.x
	obj.x = 1000 
	print obj.__dict__
	print obj.__class__.__dict__
	print obj.__class__.x
main()
	
