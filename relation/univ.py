class fact :
	def __init__(self,name) :
		self.name = name
		print self.name,' Faculty exists'
	def __del__(self) :
		print self.name,' Faculty still exists'
class dept :
	factobj = fact ('Pratyush')
	def __init__(self,name) :
		self.name = name
		print self.name,' Dept is created'
	def __del__(self) :
		print self.name,' Dept is destroyeed'
class univ :
	def __init__(self,name) :
		self.deptobj = dept('CSE')
		self.name = name
		print self.name,' is created'
	def __del__(self) :
		print 'IIT is done'
def main() :
	print 'Commencement of the university'
	univobj = univ('IIT')
	print univobj.deptobj.factobj.name
	del univobj
	print 'The end'
main()
