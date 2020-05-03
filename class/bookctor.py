class book :
	pname = 'Oxford'
	padd  = 'England'
	def __init__ (self,bname,aname,bprice,barcode) :
		self.bname = bname
		self.aname = aname
		self.bprice = bprice
		self.barcode = barcode
	def __repr__(self) :
		print self.__class__.pname
		print self.__class__.padd
		print self.bname
		print self.aname
		print self.bprice
		print self.barcode
		return 'all about the book'
def main () :
	a = book (raw_input("Enter book name : "),raw_input("Enter author name : "),input("Enter price : "),input("Enter barcode : "))
	print a
main()
