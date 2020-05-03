x = input ("Enter any number")
fun = [lambda x : x**2 ,lambda x : x**3]
if x%2 == 0 :
	print fun[0] (x)
else :
 	print fun[1] (x)
		
	
