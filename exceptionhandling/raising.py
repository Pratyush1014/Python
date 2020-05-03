if __name__ == "__main__" :
	class coffee :
		def __init__(self,temp) :
			self.temp = temp
		def drink(self) :
			if self.temp > 75 :
				raise Exception("Too hot to drink")
			elif self.temp < 25 :
				raise Exception("Too cold to drink")
			else :
				print ("Its drinkable")
	def main () :
		obj = coffee(float(input()))
		coffee.drink(obj)
	main()
