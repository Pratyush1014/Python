from person import person
class engineer(person) :
	def __init__(self,name,age,dept,salary,company) :
		person.__init__(self,name,age)
		self.dept = dept
		self.salary = salary
		self.company = company
	def __repr__(self):
		print person.__repr__(self)
		print self.dept
		print self.salary
		print self.company
		return str()
