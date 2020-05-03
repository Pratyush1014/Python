from time import ctime
from time import sleep
class mydec :
	def __init__(self,fun1) :
		self.fun1 = fun1
	def __call__(self) :
		print "Start time1 : ",ctime()
		self.fun1()
		print "Ending time1 : ",ctime()
def hello() :
	for i in range(0,5,1) :
		print 'Hello'
		sleep(1)
#@mydec
#def hi():
#	for i in range(0,5,1) :
#		print "Hi"
#		sleep(1)
obj = mydec(hello)
obj()

