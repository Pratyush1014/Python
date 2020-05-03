class printstream :
	def println (self,str) :
		print str
class System :
	out = printstream()
def main () :
	System.out.println("Hello")
main()
