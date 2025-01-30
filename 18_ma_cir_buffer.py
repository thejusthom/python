from cir_buffer import CircularBuffer

class MovingAverage(CircularBuffer):
	def __init__(self,size):
		CircularBuffer.__init__(self,size)
		self.total = 0

	def selfAverage(self):
		if self.isEmpty():
			return 0
		return self.total/self.count

	def add(self,value):
		if self.isFull():
			delta =- self.buffer[self.low]
		else:	
			delta = 0
		self.total += value
		self.total += delta
		CircularBuffer.add(self,value)

	def remove(self):
		if self.isEmpty():
			raise Exception('Circular Buffer is empty!')
		removed = CircularBuffer.remove(self)
		self.total -= removed
		return removed

	def __repr__(self):
		if self.isEmpty():
			return 'ma:[]'
		return 'ma:['+','.join(map(str,self))+']:'+str(self.selfAverage())

m = MovingAverage(3)
m.add(5)
m.add(10)
m.add(15)
m.remove()
print(m)
m.add(20)
m.add(25)
print(m)