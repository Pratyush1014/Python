#integer
obj = int()
print type(obj),obj
obj = int (10)
print type(obj),obj
obj = 10
print type(obj),obj

#Float
obj = float()
print type(obj),obj
obj = float(10.1)
print type(obj),obj
obj = 10.1
print type(obj),obj

#Long
obj = long()
print type(obj),obj
obj = long(10)
print type(obj),obj
obj = 10L
print type(obj),obj

#complex
obj = complex()
print type(obj),obj
obj = complex(10)
print type(obj),obj
obj = complex(0,11)
print type(obj),obj
obj = complex(10,22)
print type(obj),obj
obj = 11+22j
print type(obj),obj,obj.imag,obj.real
