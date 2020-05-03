a = set([1,2,3])
a.add(4)
print a
a.discard(5)
print a
a.remove(4)
print a
x = a.copy()
print x
b = set([2,3])
a = a.difference(b)
print a
a.difference_update(b)
print a
a.clear()
print a
a = set([1,2,3])
b = set([4,5,7])
c = a.union(b)
print c 
c = a.intersection(b)
print c
a.update(b)
print a
a.intersection_update(a)
a.symmetric_difference_update(b)
print a

