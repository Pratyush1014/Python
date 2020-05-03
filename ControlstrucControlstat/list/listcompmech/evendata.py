list = [1,-50,-67,23,54,56,7,98,54,32,12,34,56,78,8,9,90,67,54,3,2,2,34,56,7,8,89,9]
new = []
[new.append(data) for data in list if data%2==0 and data not in new]
print new
