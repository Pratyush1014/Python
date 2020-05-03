def chgen () :
	list = ['sony','BBC','HBO','select','cc']
	for i in list :
		yield i
def main () :
	n = input("channel number : ")
	remote = chgen()
	for i in range(n) :
		channel = remote.next()
	print channel
main()
