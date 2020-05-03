class alpha :
	def __init__(self) :
		print "class is called"
		return None
	def __call__(self) :
		print "oblect is called"
	def __repr__(self) :
		return "tried to print the object"

def main() :
	alpha()
	obj = alpha() 
	obj()
	print obj

main()
