class complx :
	def __init__(self,data1=0,data2=0) :
		self.real = data1
		self.img = data2
	def __repr__(self) :
		print 'complex number : ',self.real,' + i',self.img
		return str()
	def __add__(self,other):
		res = complx()
		res.real = self.real + other.real
		res.img = self.img+other.img
		return res
	def __sub__(self,other) :
		res = complx()
		res.real=self.real-other.real
		res.img = self.img-other.img
		return res
	def __mul__(self,other) :
		res = complx()
		res.real = self.real*other.real - self.img*other.img
		res.img = self.real*other.img+self.img*other.real
		return res
	def __del__(self):
		print 'complex has been neutralized'

def main() :
	a = complx(12,14)
	print a
	b = complx(15,21)
	print b
	sum = a+b
	print 'sum is : ',sum
	sub = a-b
	print 'sub is : ',sub
	mult= a*b
	print 'mult is : ',mult
	del a
	del b
main()
