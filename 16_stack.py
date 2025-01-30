class Stack:
	def __init__(self):
		self.stack = []

	def push(self,v): #O(N)
		print("Pushing "+str(v))
		return self.stack.append(v)

	def pop(self): #O(N)
		if(self.isEmpty()):
			raise Exception('Stack is empty')
		print("popping...")
		return self.stack.pop()


	def isEmpty(self):
		return len(self.stack) == 0 #O(N)

	def __repr__(self):
		print(self.stack)

s = Stack()
s.push(5)
s.pop()
s.__repr__()
s.push(5)
s.push(11)
s.push(10)
s.__repr__()