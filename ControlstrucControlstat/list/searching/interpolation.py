list = [1,3,4,6,7,2,9,10,11]
print type(list)
print list[1]
p = len(list)
list = list.sort()
s = input("Enter input to search ")
l = 0
h = p-1
pos = l + ((s - list[l])/(list[h]-list[l]))*(h-l)
print list [pos]
