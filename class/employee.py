from random import randint
class employee :
	#nonstatic method
	def createemp(self) :
		name = raw_input("Enter name : ")
		age = input("Enter age : ")
		salary = input("Enter salary : ")
		id = self.autogenid()
		print 'Employee id is : ',name + id
	@classmethod
	def createbase (cls) :
		cname = raw_input("Ente your company name : ")
		cid = cls.autogenid()
		print 'company id is : ',cname+cid
	@staticmethod
	def autogenid () :
		id = str(randint(1200456,3245676))
		return id
def main () :
	object = employee()
	object.createemp()
	employee.createbase()
main()
