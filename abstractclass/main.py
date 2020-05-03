from abs import shape
class square(shape) :
	def __init__(self,a,b) :
		self.a = a
		self.b = b 
	def area(self) :
		return self.a*self.b
	def perimeter(self) :
		return self.a + self.b
def main () :
	obj = square(10,24)
	print (obj.area())
	print (obj.perimeter())
main()
#compile it using python 3
