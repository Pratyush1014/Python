from sys import getrefcount
class object :
	def __init__(self,x) :
		self.name = x
	def __repr__(self) :
		str = self.name + 'Has been created'
		return str
	def __del__(self) :
		print self.name,' Object has been destroyed'
def main() :
	obj = object('Parent')	
	print obj
	x = object('x')
	print x
	y = object('y')
	print y
	z = object('z')
	print z
	x = obj;
	print 'x -> object'
	y = x
	print 'y -> object'
	z = y
	print 'z -> object'
	print 'refcount is  : ',getrefcount(obj)
	del x
	print 'refcount is  : ',getrefcount(obj)
	del y
	print 'refcount is  : ',getrefcount(obj)
	del z
	print 'refcount is  : ',getrefcount(obj)
	print 'Garbage collector is invoked thus its an orphan object'
main() 
	
