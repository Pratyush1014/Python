result = None
a = float(input())
b = float(input())

try :
	result = a/b 
except Exception as e:
	print ("Cant process some error occured due to ",e)
print ("Well processed")
print (result)
