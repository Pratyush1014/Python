from time import *
class math :
	def __init__ (self,function) :
		self.function = function
	def __call__ (self) :
		print "start ",ctime()
		self.function()
		print "stop ",ctime()
@math
def hi () :
	for i in range (1,6,1) :
		print "hi"
		sleep(1)
def main() :
	obj = math(hi)
	obj()
main()
