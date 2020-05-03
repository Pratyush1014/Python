def main() :
	print "1-to add 2-to sub 3-multiply"
	ch=input("Enter choice :")
	if ch == 1 :
		execute(add)
	if ch == 2 :
		execute(sub)
	if ch == 3 :
		execute(multiply)
def execute (fun ) :
	fun (input(),input())
def add (x,y) :
	print x+y
def sub(x,y) :
	print x-y
def multiply (x,y):
	print x*y
main()


