class Node :
	def __init__(self,data) :
		self.data = data
	def __sub__(self,next) :
		self.ad = next
		return next
def main():
	a = Node (10)
	b = Node (20)
	c = Node (30)
	d = Node (40)
	e = Node (50)
	a-b-c-d-e
	print a.data
	print a.ad.data
	print a.ad.ad.data
	print a.ad.ad.ad.data
	print a.ad.ad.ad.ad.data
main()
