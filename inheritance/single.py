class person :
	def __init__(self,name,age) :
		self.name = name
		self.age = age
	def __repr__(self) :
		return self.name+" "+str(self.age)
class student (person) :
	def __init__(self,name,age,mark,regid):
		person.__init__(self,name,age)
		self.mark = mark
		self.regid = regid
	def __repr__(self) :
		return person.__repr__(self)+" "+str(self.mark)+" "+str(self.age)
def main() :
	obj = student("Alpha",13,98,1234)
	print obj
main()

