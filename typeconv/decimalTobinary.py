class decimal :
	def __init__(self,other=0) :
		if other.__class__ == int :
			self.data = other
		elif other.__class__ == binary :
			self.data = 0
			while other.data != 0 :
				self.data = (self.data)*2 + (other.data)%10
				other.data = (other.data)/10
	def __repr__(self) :
		return str(self.data)
class binary :
	def __init__(self,other=0) :
		if other.__class__ == int :
			self.data = other
		elif other.__class__== decimal :
			self.data = 0
			while other.data!=0 :
				self.data = (self.data)*10 + (other.data)%2
				other.data = (other.data)/2
	def __repr__(self) :
		return str(self.data)
def main () :
	a = decimal(5)
	c = binary(1010)
	b = binary(a)
	print b
	d = decimal(c)
	print d
main()
	
