class a:
	def home(self,an) :
		self.an = an
		print "You have accessed an of a"
class b(a):
	def home(self,an,bn):
		self.bn=bn
		print "You have accessed thru b"
		a.home(self,an)
class c(a):
	def home(self,an,cn) :
		self.cn =cn
		print "You have accessed thru c"
		a.home(self,an)
class d(b,c):
	pass
def main () :
	obj  =d()
	d.home(obj,10,12)
main()

