x = [1,2,3,4,5,6,7,8,9]
print x	
x.append(10)
print x
x.pop(9)
print x
x.append(11)
print x
x.remove(11)
print x
y = [10,11]
x.append(y)
print x
del x[9][1]
print x
x.remove(y)
print x
y=[10,11,12]
x.extend(y)
print x
x.insert (1,100)
print x
x.sort()
print x
x.sort(reverse = True)
print x
i=x.index(100)
print x#prints the entire list
print i
x.append(100)
print x
c = x.count(100)
print c
z=[1,2,3,4,5,6]
a=z.reverse()#doesn't return anything
print z,a


