from random import randint
from time import sleep
class mail :
	tag = '@iitg.ac.in'
	def __init__(self,name) :
		self.name = name
	def __getuid(self) :
		self.uid = self.name+self.tag
		return self.uid
	def __getpwd(self) :
		self.pwd = self.autogenpwd(self.name)
		return self.pwd
	def permission(self,pd) :
		print "wait for a few secs till we process your request"
		sleep(2)
		if pd == 'Hell_Hitler':
			print self.__getuid()
			print self.__getpwd()
		else :
			print 'You have entered an invalid password'
	@staticmethod
	def autogenpwd(name) :#static method
		return name+str(randint(1200,1234)).zfill(6)
def main() :
	obj = mail(raw_input("Enter your name : "))
	print 'Your request is being processed'
	sleep(2)
	mail.permission(obj,raw_input("Enter the master password to enter : "))
main()
