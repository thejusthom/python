class CircularBuffer:
	def __init__(self,size):
		self.buffer = [None]*size
		self.size = size
		self.low = 0
		self.high = 0
		self.count = 0

	def isEmpty(self):
		return self.count == 0

	def isFull(self):
		return self.count == self.size

	def add(self,value):
		if self.isFull():
			self.low = (self.low+1) % self.size
		else:
			self.count += 1
		self.buffer[self.high] = value
		self.high = (self.high+1) % self.size

	def remove(self):
		if self.isEmpty():
			raise Exception('Empty Circular Buffer!')
		self.count -= 1
		value = self.buffer[self.low]
		self.low = (self.low + 1) % self.size
		return value

	def __iter__(self):
		idx = self.low
		num = self.count
		while num > 0:
			yield self.buffer[idx]
			idx = (idx+1) % self.size
			num -=1

	def __repr__(self):
		if(self.isEmpty()):
			return 'cb:[]'
		return 'cb:['+','.join(map(str,self))+']'



# c = CircularBuffer(5);
# c.isEmpty()
# c.add(5)
# c.add(10)
# c.add(7)
# c.add(2)
# print(c)
# print(c.remove())
# print(c)
# c.add(17)
# c.add(25)
# c.add(35)
# print(c)





