from os import * 
from time import sleep 

def main () : 

	r , w = pipe () 	

	k = fork () 
	
	if k == 0 : 
		write ( w , 'hello parent i am your child ')
		while 1:
			print 'i am child '
			sleep (1)
	
	else :		
		data = read ( r , 100  ) 

		while 1 : 
			print 'i am parent ', data 
			sleep (1)

main ()
