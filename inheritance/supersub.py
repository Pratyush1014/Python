from super import person as p
class man(p) :
	def __init__(self,name,age) :
		super().__init__(name)
		self.age = age
	def __repr__(self) :
		print (super().__repr__())
		print (self.age)
		return str()
def main() :
	obj = man("alpha",45)
	print (obj)
	print (obj.mro())
main()
