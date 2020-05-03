class zep :
	def __init__(self,a,b) :
		self.real = a
		self.imag = b
	def __add__(self,other) :
		if other.__class__ == int :
			print "zep + int"
			self.real = self.real + other
			self.imag = self.imag
			return self
		elif other.__class__ == self :
			print "zep + zep"
			res = super()
			res.real = self.real + other.real
			res.imag = self.imag + other.imag
			return res
	def __radd__(self,other) :
			print "int + zep"
			self.real = self.real + other
			self.imag = self.imag
			return self
class super :
	def __init__(self,a) :
		if a.__class__ == int :
			self.real = a
			self.imag = 0
		elif a.__class__ == zep :
			self.real = a.real
			self.imag = a.imag
		elif a.__class__ == super :
			self.real = a.real
			self.imag = a.imag
	def __repr__(self) :
		if self.imag != 0 :
			print str(self.real)+"+j"+str(self.imag)
			return str() 
		print self.real
		return str()
			
def main () :
	a = int (10)
	b = int (20)
	c = zep (11,22)
	d = zep (23,34)
	e = super(a+b)
	print e 
	e = super(a+c)
	print e 
	e = super(c+b)
	print e 
	e = super(c+d)
	print e 
main()
