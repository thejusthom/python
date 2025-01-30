# Print Hello world!
import sys

x=5
y=10
greeting = 'Hey'
name = 'Thejus'
message = ('{}, {}. Welcome!').format(greeting,name)
print(message)
message = f'{greeting}, {name.upper()}. Welcome with F String!'
# print(dir(message))
print(help(str.replace))
print(message)
print(sys.version)
if x>y:
	print('x>y')
else:
	print('else')

