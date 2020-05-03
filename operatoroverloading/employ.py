class employ :
	def __init__(self,name,age):
		self.ename = name ;
		self.age = age ;
	def __ge__(self,other) :
		if self.age > other.age :
			self,other = other,self
	def __repr__(self) :
		return str(self.ename)+' '+str(self.age)
def sort (emp,n) :
	for i in range(n) :
		for j in range (i+1,n) :
			if emp[i]>emp[j] :
				emp[i],emp[j]=emp[j],emp[i]
def main() :
	n = input("Enter number of entries : ")
	emp = []
	for i in range(n) :
		e = employ(raw_input("Enter name : "),input("Enter age : "))
		emp.append(e)
	sort(emp,n)
	print emp
main()

	
