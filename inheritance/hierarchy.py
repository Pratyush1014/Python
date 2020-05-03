class a:
	def __init__(self,no) :
		self.no = no
	def __repr__(self) :
		return str(self.no)
class b(a):
	def __init__(self,no) :
		a.__init__(self,no)
		print "You have accessed thru b"
	def __repr__(self) :
		return str(self.no)
class c(a):
	def __init__(self,no) :
		a.__init__(self,no)
		print "You have accessed thru c"
	def __repr__(self) :
		return str(self.no)
def man():
	obja = a(12)
	print obja	
	objb = b(10)
	print objb
	print obja
	objc = c(20)
	print objc
	print obja
	print objb
man()


