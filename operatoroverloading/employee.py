class emp :
	@classmethod
	def create (cls) :
		cls.cname = raw_input("Set company name : ")
		cls.add = raw_input("Set add : ")
	def __init__(self) :
		self.name = raw_input('Enter name : ')
		self.age = input('Enter age : ')
	def __repr__(self) :
		return str(self.name)+' '+str(self.age)
def age_sort(employee,n):
	for i in range(n):
		for j in range(i+1,n):
			if employee[i].age>employee[j].age :
				temp = employee[i]
				employee[i] = employee[j]
				employee[j] = temp
	return employee
		
			
def main() :
	employee=[]
	emp.create()
	n = input("how many ?")
	for i in range (n):
		e = emp()
		employee.append(e)
		
	employee = age_sort(employee,n)
	print employee
main()
