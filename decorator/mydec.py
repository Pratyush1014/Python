from time import ctime
from time import sleep
class mydec :
	def __init__(self,fun1) :
		self.fun1 = fun1
	def __call__(self,nmae) :
		print "Start time1 : ",ctime()
		self.fun1(nmae)
		print "Ending time1 : ",ctime()
def hello(name) :
	for i in range(0,5,1) :
		print 'Hello',name
		sleep(1)
@mydec
def hi(name):
	for i in range(0,5,1) :
		print "Hi",name
		sleep(1)
obj = mydec(hello)
obj('alpha')
obj = mydec(hi)
hi('delta')
