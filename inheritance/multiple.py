class a:
	def method (self) :
		print "you are acessing the resources of class a"
		
class b:
	def method(self) :
		print "You are acessing the resources of class b"
class c(a,b):#more priority is given to a
	pass
def main():
	obj = c()
	c.method(obj)#since a is given more priority it is accessed first
	b.method(obj)
main()

