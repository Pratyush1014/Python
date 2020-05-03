from random import randint
class test :
	#nonstaticmethod
	def create (self):
		name = raw_input("Enter your company name")
	def createid(self):
		regid = self.autogenid()
		print 'Generated id for your company is : ',regid
	def autogenid(self) :
		regid = 'self.name' + str(randint(1956,5678)).zfill(6)
		return regid
def main():
	print 'contents of class',test.__dict__
	object = test()
	test.create(object)
	test.createid(object)
main()
		
