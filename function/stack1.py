def push (stack,sp) :
	if sp == 4 :
		print "stack is full "
	else :
		sp += 1
		stack [sp] = input("Data to be pushed :")
	return sp 
def pop (stack,sp) :
	if sp == -1 :
		print "stack is empty "
	else :
		stack[sp] = 0
		sp -= 1
	return sp
def display (stack,sp) :
	for i in range (sp,-1,-1) :
		print stack[i],
def main() :
	stack = [0,0,0,0,0]
	sp = -1
	while True :
		print
		ch = input("1-push 2-pop 3-exit :")
		if ch == 1 :
			sp=push(stack,sp)
			display(stack,sp)
		elif ch == 2 :
			sp = pop(stack,sp)
			display(stack,sp)
		elif ch == 3 :
			break
		else :
			print "invalid entry "
main()



	
