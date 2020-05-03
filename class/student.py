from random import randint
from login import login
class student :
	@classmethod 
	def parent (cls) :
		cls.school = raw_input("Enter school name : ")
		cls.address = raw_input("Enter address : ")

	def ward (self) :
		self.name = raw_input("Enter name : ")
		self.std = input("Enter std : ")
		self.id = self.generateid(self)
		
	@staticmethod
	def generateid(student) :
		if student.__class__.school == "MPS" :
			ids = 001 
		id = str(ids) + student.name + str(randint(1345,3445)).zfill(7)
		return id

	def read(self) :
		print self.__class__.school
		print self.__class__.address
		print self.name
		print self.std
		print self.id
def createdatabase (student) :
	list = [student.parent(),student.ward()]
	for i in list :
		i
def main () :
	obj1 = student()
	createdatabase (obj1)
	obj1.read()
	login()
main()
