stack = [ 0, 0, 0, 0, 0 ]
sp = -1
def stack_full () :
	global stack
	global sp
	if sp == 5 :
		print "Stack is full"	
		return True
	else :
		return False
def stack_empty () :
	global stack
	global sp
	if sp == -1 :
		print "stack is empty"
		return True
	else :
		return False
def push () :
	global stack
	global sp
	data = input("Enter data to be pushed : ")
	sp+=1
	stack[sp] = data
	#stack.append(data)
def pop() :
	global stack
	global sp
	sp+=-1
def display () :
	global stack
	global sp
	for i in stack :
		print i,
def main() :
	global stack
	global sp
	while True :
		print "1-push 2-pop 3-exit"
		ch = input("Enter choice") 
		if ch == 1 :
			if stack_full():
				display()
				continue
			else :
				push()
				display()
		if ch == 2 :
			if stack_empty() :
				continue
			else :
				pop()
				continue

		if ch == 3 :
			exit(0)
main()
