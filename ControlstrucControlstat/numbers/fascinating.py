n = input ("Enter any number :")
x = n*1
y = n*2
z = n*3
a = str(x)+str(y)+str(z)
b = list(a)
b.sort()
c = ''.join(b)
if c == '123456789' :
	print "Fascinating"
else :
	print "Not"
