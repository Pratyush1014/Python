class email :
	domain = '@iitg.ac.in'
	def __init__(self,uid,pwd):
		self.uid = uid+email.domain
		self.__pwd = pwd#password becomes private
	def __getpwd(self):
		return self.__pwd
	def getpubpwd(self) :
		return self.__getpwd()
def main() :
	obj = email('Pratyush','fyu99232')
	print obj.uid
	#print obj.__pwd error since password is private
	#obj.__getpwd() error since getpwd is private
	print obj.getpubpwd()
main()
