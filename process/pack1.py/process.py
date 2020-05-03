from time import sleep
from os import system
from os import getpid 
def main () :
	count = 0
	while True :
		print 'Hello ',count
		if count == 5 :
			system('kill '+str(getpid()))
		count += 1
		sleep(1)
main ()
		
