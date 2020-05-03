class bit :
	def __init__(self,b) :
		if b.__class__==int :
			print 'int to bits'
			self.bits = b
		elif b.__class__==byte :
			print 'bytes to bits'
			self.bits = b.bytes*8
	def __repr__(self) :
		return str(self.bits) + 'bits'
class byte :
	def __init__(self,b) :
		if b.__class__==int :
			print 'int to bytes'
			self.bytes = b
		elif b.__class__==bit :
			print 'bits to bytes'
			self.bytes = b.bits/8
	def __repr__(self) :
		return str(self.bytes) + 'bytes'
def man():
	a = bit (32)
	print a
	b = byte (8)
	print b
	x = byte(a)
	print x
	y = bit (b)
	print y
man()

		
