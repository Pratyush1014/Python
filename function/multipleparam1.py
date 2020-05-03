def printperson (**person) :
	print person ,type(person)
	print 'information about : ',person['name']
	for key in person :
		print key ,person[key]
def main () :
	printperson(name='alpha')
	printperson(name='beta',age=23)
	printperson(name='charlie',age=25,id=3)
main()
