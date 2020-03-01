# lists, indexing, slicing and methods
courses_1 = ['history', 'math', 'physics']
print(len(courses_1))
print(courses_1)
print(courses_1[0])
print(courses_1[-1])
print(courses_1[0:2])
print(courses_1[:2])
print(courses_1[1:])
courses_1.append('art') # added to the end
courses_1.insert(0,'compsci') # inserted to position 0
courses_2 = ['education']
courses_1.extend(courses_2)
courses_1.remove('math')
courses_1.pop() # removes last value
courses_1.reverse()
courses_1.sort()
print(courses_1)
numbers_1 = [1,5,3,2,4]
numbers_1.sort(reverse=True)
print(numbers_1)
print(sorted(courses_1))
print(min(numbers_1))
print(max(numbers_1))
print(sum(numbers_1))
print(courses_1.index('art'))
print('art' in courses_1)
for item in courses_1: print(item)
for index, item in enumerate(courses_1): print(index, item)
for index, item in enumerate(courses_1, start=1): print(index, item)
courses_1_string = ','.join(courses_1)
print(courses_1_string)
courses_3 = courses_1_string.split(',')
print(courses_3)

# tuples - immutable lists
list_1 = ['a', 'b', 'c']
list_2 = list_1
list_1[0] = 'x'
print(list_1)
print(list_2)
tuple_1 = ('ta', 'tb', 'tc')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

# sets
set_1 = {'a', 'b' , 'd', 'c', 'a'}
print(set_1)
print('a' in set_1)
set_2 = {'c', 'd', 'e', 'f'}
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_1.union(set_2))

# creating empty objects
empty_list = []
empty_list = list()
empty_tuple = ()
empty_tuple = tuple()
empty_set = {} # incorrect; this is a dictionary
empty_set = set() # correct; this is a set

