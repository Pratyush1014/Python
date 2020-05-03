list = [1,2,2,5,4,7,4,6,9,0,87,5,3,2,5,7,8,5,4,3,2,2,5,6,78]
new = []
[new.append(data) for data in list if data not in new]
print new
