# courses = ['Abc','Bcd','Cde','Def']
# courses_2 = ['Zyx','Yxw']
# print(courses)
# print(courses[-1])
# print(courses[0:2])
# print(courses[:2])
# print(courses[2:])
# print(help(courses))
# courses.append('Efg')
# courses.insert(0,courses_2)
# courses.append(courses_2) # same as insert
# courses.extend(courses_2)
# courses.remove('Abc')
# print(courses)
# popped = courses.pop()	
# print(popped)
# print(courses)
# courses.reverse()
# print(courses)
# courses.sort()
# print(courses)
# courses_num = [1,66,2,9,6,1]
# courses_num.sort()
# print(courses_num)
# courses_num.sort(reverse=True) # also applicable to list of string
# print(courses_num)

# to sort and save in diff list
# sc = sorted(courses)
# print(courses)
# print('Bcd' in courses)
# print(sc)
# print(sum(courses_num))

# courses_str = ' - '.join(courses) # converts list to string and prints the ' - '
# print(courses_str)

# reverses it
# new_list = courses_str.split(' - ')
# print(new_list)

# for x in courses:
# 	print (x)

# for i,x in enumerate(courses,start=1):
# 	print (i,x)	

# tuples are basically immutable new_list
list1 = ['a','b','c']
list2 = list1

list1[0] = 'z'

print(list1)
print(list2)

tuple1 = ('a','b','c')
tuple2 = tuple1

# tuple1[0] = 'z' #error

print(tuple1)
print(tuple2)

# set used to remove duplicates
# can be used to find common, different elements
set1 = {'a','b','c','c'}
set2 = {'a','b','d','e'}
print(set1) # order keeps changing each execution
print(set1.intersection(set2))	
print(set1.difference(set2))
print(set1.union(set2))