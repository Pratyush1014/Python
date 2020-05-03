cy = input("Enter current year : ")
cm = input("Enter current month : ")
cd = input("Enter current date : ")

py = input("Enter birth year : ")
pm = input("Enter birth month : ")
pd = input("Enter birth date : ")

if cd > pd :
	td = cd - pd
else :
	if cm in [1,3,5,7,8,10,12] :
		td = cd + 31 - pd
	elif cm in [4,6,9,11] :
		td = cd + 30 - pd
	else :
		if cy%4 == 0 :
			if  cy %100 == 0 :
				if cy %400 == 0 :
					td = cd + 29 - pd
				else :
					td = cd + 28 - pd
			else :
				td = cd + 28 - pd
		else :
			td = cd + 28 -pd
	cm -= 1
if cm >pm :
	tm = cm - pm
else :
	tm = cm + 12 - pm
	cy -= 1
ty = cy - py
print "Your age till today is ",ty," yrs",tm," months",td," days"
