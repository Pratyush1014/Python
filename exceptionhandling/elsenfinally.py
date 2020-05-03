result = None
a = float(input())
b = float(input())

try :
	result = a/b 
except Exception as e :
	print ("Error due to ",e)
else :
	print ("Errorless")
	print(result)
finally :
	print ("Your job is done")
