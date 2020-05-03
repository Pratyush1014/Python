class Node :
	def __init__(self,data) :
		self.data = data
	def __sub__(self,next) :
		self.adn = next
		next.adp = self
		return next
def main():
	a = Node (10)
	b = Node (20)
	c = Node (30)
	d = Node (40)
	e = Node (50)
	a-b-c-d-e-a
	print a.data
	print a.adp.data
	print a.adp.adp.data
	print a.adp.adn.adp.data
	print a.adn.adn.adn.adn.data
main()
