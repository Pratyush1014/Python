class parent:
	def home(self) :
		print "Welcome to parent's house"
	def food(self) :
		print "you dont have money"
		print "You can eat my free food"
class son(parent) :
	def home(self) :#overrides parent's home
		print "I have my own house"
	def food (self,price) :#overrides parent's food
		print "I will pay the price and eat"
def main() :
	obj = son()
	obj.home()
	obj.food(100)
	#obj.food() error since parent's food is hiden
	parent.food(obj)
main()
