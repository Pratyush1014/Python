class Node :
	def __init__(self,data) :
		self.data = data
	def __add__(self,other) :
		self.next = other
		return other
	def __repr__(self) :
		print self.data
		return str()
def main () :
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)
	e = Node(5)
	f = Node(6)
	g = Node(7)
	
	a+b+c+d+e+f+g
	
	print a
	print a.next
	print a.next.next
	print a.next.next.next
main()
