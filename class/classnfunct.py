def create_man (a) :
	a.name = raw_input("Enter name : ")
	a.age = raw_input("Enter age : ")
	a.height = raw_input("Enter height : ")
class man :
	'''This is all you wanna know about a man'''	
def main() :
	a = man()
	create_man(a)
	print a.__dict__
	man.gender = "Male"
	print a.__dict__
	print man.__dict__
	print getattr(a,'gender')
main()
