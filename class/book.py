from random import randint
class book :
	@classmethod
	def createStatdata(cls) :
		cls.pname = None
		cls.padd = None
	def createNsdata (self) :
		self.bname = None
		self.bprice = None
		self.barcode = self.autogenbar()
		self.aname = None
	def read(self) :
		print self.bname
		print self.bprice
		print self.barcode
		print self.aname
		print self.__class__.pname
		print self.__class__.padd
	@staticmethod
	def autogenbar ():
		bar = str(randint(1000,3000)).zfill(6)
		return bar
def main() :
	a = book()
	a.createStatdata()
	book.createNsdata(a)
	book.read(a)
main()
