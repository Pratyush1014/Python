def func(**x) :
	print "Infos about ",x['name']
	for key in x :
		print key,x[key]
def main () :
	func (name="alpha",age=23,dept="cse")
main()
