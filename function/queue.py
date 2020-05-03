def enq (q,fp,rp) :
	if rp == 4 :
		print "q is full"
	elif rp==fp==-1 :
		rp+=1
		fp+=1
		q[rp] = input("Enter 1st data to be queued")
	else :
		rp +=1
		q[rp] = input("Enter data to be queued")
	return fp,rp
def deq (q,fp,rp) :
	if rp==fp==-1 :
		print "q is empty"
	elif fp==rp==0 :
		q[rp] = 0
		fp=-1
		rp=-1
	else :
		k = fp
		while k<rp :
			q[k] = q[k+1]
			q[k+1] = 0
			k+=1
		q[rp] = 0
		rp -=1
	return fp,rp
def display (q,fp,rp) :
	print [i for i in q if i!=0]
def main () :
	q = [0,0,0,0,0]
	fp = -1
	rp = -1
	while True :
		print
		ch = input("1-enq 2-deq 3-exit :")
		if ch == 1 :
			fp,rp = enq(q,fp,rp)
			display(q,fp,rp)
		elif ch == 2 :
			fp,rp = deq(q,fp,rp)
			display(q,fp,rp)
		elif ch == 3 :
			break 
		else :
			print "Invalid entry "
main()
