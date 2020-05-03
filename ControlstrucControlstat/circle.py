cx = input("Enter the origin x : ")
cy = input("Enter the origin y : ")
r = input("Enter the radius of the circle :")
px = input("Enter the x cod : ")
py = input("Enter the y cod : ")
d = ((cx-px)*(cx-px) + (cy-py)*(cy-py))**0.5
if d>r :
	print "OUTSIDE"
elif d==r :
	print "ONTHE"
else :
	print "INSIDE"
