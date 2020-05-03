top = -1
stack = [0,0,0,0,0] 
def push () :
	global top
	global stack
	if top == 4 :
		print "stack is full"
		return 
	data = input("Enter data to push : ")
	top +=1
	stack[top] = data
def pop () :
	global top
	global stack
	if top == -1 :
		print "stack is empty"
		return
	top -=1
def traverse () :
	global top 
	global stack 
	for data in range(0,top+1,1) :
		print stack[data]
	print 
def main() :
	while True :
		print "1-Push 2-Pop 3-Exit"
		ch = input("Enter your choice : ")
		if ch == 1 :
			push()
			traverse()
		elif ch == 2 :
			pop()
			traverse()
		elif ch == 3 :
			exit(0)
		else :
			print "Default entry"
main()
