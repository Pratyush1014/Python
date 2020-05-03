x = input('Enter the first number : ')
y = input('Enter the second number : ')
z = input('Enter the third number : ')
w = x if x>z else z if x>y else y if y>z else z
print "Max of 3 is ",w
