class a:
	pass
class b(a):
	def locate(self) :
		print "Python searches thru DFS mech"
class c:
	def locate(self) :
		print "Python searches thru BFS mech"
class d(a,b):
	pass
def main() :
	obj = d()
	d.locate(obj)
main()
	
