class teacher :
	def __init__(self) :
		print "Teacher Exists"
	def __del__(self) :
		print "Teacher's existence has no meaning"
class standard :
	beta = teacher()
	def __init__(self) :
		print "standard is created "
	def __del__(self) :
		print "standard is destroyed"
class school :
	def __init__ (self,name) :
		print "School is created "
		self.standardobj = standard()
	def __del__(self) :
		print "school is destroyed"
def main() :	
	obj = school("Alpha")
main()
	
