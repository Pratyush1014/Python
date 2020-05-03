class Hot(Exception) :
	def __init__(self,msg) :
		super().__init__(msg)
class coffee :
	def __init__(self,temp) :
		self.temp = temp 
	def drink(self) :
		if self.temp > 75 :
			raise Hot ("TOO HOT")
		else :
			print ("Drinkable")
def main() :
	obj = coffee (int(input()))
	obj.drink()
main()		
