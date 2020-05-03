str = "India is my country"
h = len(str)-1
rev = []
[rev.append(str[i]) for i in range(h,-1,-1)]
print ''.join(rev)
print rev
s = [][]
i = 0
j = 0
while i<h :
	if rev[i] != ' ':
		s[j].append(rev[i])
		i+=1
	else :
		i+=1
		j+=1

