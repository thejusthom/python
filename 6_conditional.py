user = 'Admin'
logged=False

if user == 'Admin' and logged == True:
	print('Admin Login Successful')
elif user == 'User' and logged == True:
	print('User Login Successful')
else:
	print('Login Failed, try again!')


a = [1,2,3]
b = [1,2,3]
# b = a
b
if a == b:
	print('equal')	
	print(id(a))
	print(id(b))
if a is b:
	print('is')

# False values
# False, None, 0 of any numeric, empty list, tuple, set, map
# Everything else is true	