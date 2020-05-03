a = dict({1:'one',2:'two',3:'three'}) 
print a
print a.keys()
print a.values()
print a.items()
r =a.iterkeys()
print r,r.next()
k = a.iteritems()
print k , k.next()
a.pop(1)
print a
a.popitem()
print a
a.clear()
print a
