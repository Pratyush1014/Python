from sys import getrefcount
class animal :
	def __init__(self,type,breed) :
		self.setting(type,breed)
		return None
	def setting(self,type,breed) :
		self.type = type 
		self.breed = breed
	def __repr__(self) :
		print self.type
		print self.breed
		return str()
	def __del__(self) :
		print "Link to obj is getting destroyed"
def main () :
	obj = animal(raw_input("Enter type : "),raw_input("Enter breed : "))
	print obj
	x = obj 
	y = x 
	z = obj
	print getrefcount(obj)
	del(x)
	print getrefcount(obj)
	del(y)
	print getrefcount(obj)
	del(z)
	print getrefcount(obj)
	del(obj)
	print "Finally its destroyed"

main()
	
