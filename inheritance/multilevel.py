class university :
	def __init__(self,org) :
		self.org = org
	def __repr__(self) :
		return self.org
	def salary(self):
		print 'University is going to pay you your salary'
class department(university) :
	def __init__(self,org,dept):
		university.__init__(self,org)
		self.dept = dept
	def __repr__(self) :
		return university.__repr__(self)+' '+self.dept
	def salary(self,thesis):
		print 'Department is going to pay you your salary'
class faculty(department) :
	def __init__(self,name,org,dept) :
		department.__init__(self,org,dept)
		self.name = name
	def __repr__(self) :
		return department.__repr__(self)+' '+self.name
def main() :
	obj = faculty("Pratyush","IIT","CSE")
	print obj
	department.salary(obj,10)#Overriding of salary method of university class
	university.salary(obj)#if there wasn't any inheritance you couldn't have passed the object of faculty class

main()
