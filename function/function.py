def main () :
	anumber = 10
	print 'anumber :',anumber,id(anumber)
	numberf(anumber)
	print 'anumber :',anumber,id(anumber)
	alist = [1,2,3,4,5]
	print 'alist :',alist,id(alist)
	listf(alist)
	print 'alist :',alist,id(alist)
	atuple = (1,2,3,4,5)
	print 'atuple :',atuple,id(atuple)
	tuplef(atuple)
	print 'atuple :',atuple,id(atuple)
	aset = set([1,2,3,4,5])
	print 'aset :',aset,id(aset)
	setf(aset)
	print 'aset :',aset,id(aset)
	dic = {1:'a',2:'b',3:'c',4:'d'}
	print 'adic :',dic,id(dic)
	dicf(dic)
	print 'adic :',dic,id(dic)
def numberf (fnumber) :
	print 'fnumber :',fnumber ,id(fnumber)
	fnumber = fnumber +10
	print 'fnumber :',fnumber ,id(fnumber)
def listf (flist) :
	print 'flist :',flist ,id(flist)
	flist.append(6)
	print 'flsit :',flist ,id (flist)
def tuplef (ftuple) :
	print 'ftuple :',ftuple, id(ftuple)
	lup = ('a',)
	ftuple += lup
	print 'ftuple :',ftuple ,id(ftuple)
def setf (fset) :
	print 'fset :',fset ,id(fset)
	fset.add(6)
	print 'fset :',fset ,id(fset)
def dicf (dic) :
	print 'fdic :',dic ,id(dic)
	dic.popitem()
	print 'fdic :',dic ,id(dic)
main()
