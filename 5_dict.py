stud = {} #this is empty dict, not empty set
stud = {'name':'Thejus', 'age':26, 'course':['Math','Science'],1:'one',2:'two'}
print(stud)
print(stud['name'])
# print(stud['phone']) # error, to prevent this
print(stud.get('name'))
print(stud.get('phone')) # no error, just None

stud['phone'] = '861-038-830'
stud['name'] = 'Thomson' # updates
print(stud.get('name','Not found!')) # set default not found
stud.update({'name':'Thejus','age':28,'phone':999999999}) # update mutiple values at once	

# deleting dict
del stud[1]
deleted = stud.pop(2)

print(deleted)
print(stud)

print(stud.get('name','Not found!')) # set default not found
print(stud.get('phone','Not found!')) # set default not found

#printing dicts
print(stud.keys())
print(stud.values())
print(stud.items())
# finding length of dict
print(len(stud))

# looping
for key,values in stud.items():
	print(key, values)



