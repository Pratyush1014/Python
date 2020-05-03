from person import person
class doctor(person) :
	def __init__ (self,name,age,desg,stream) :
		person.__init__(self,name,age)
		self.desg = desg
		self.stream = stream
	def __repr__(self) :
		print person.__repr__(self)
		print self.desg
		print self.stream
		return str()

