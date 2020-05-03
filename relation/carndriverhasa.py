class driver :
        def __init__(self,name):
        	self.name = name
                print 'Driver is aval'
        def __del__(self) :
                print 'Driver not available'
class car :
	driverobj = driver('alpha')
	def __init__(self) :
		print 'Car is there'
		self.engineobj = engine()
	def __del__(self):
		print 'Car is not there'
		
class engine :
	def __init__(self) :
		print 'Engine is running'
	def __del__(self) :
		print 'Engine is not running'
def main() :
	print 'Start'
	carobj = car()
	print carobj.driverobj.name
	del carobj
	print 'end'
main()
