# setting up a dictionary
student = {'name': 'John', 'age': 25, 'courses': ['math','compsci']}

# read values from a dictionary
print(student)
print(student['name'])
print(student['courses'])
#print(student['phone']) # results in error
print(student.get('name'))
print(student.get('phone')) # results in none
print(student.get('phone', 'not found')) # results in not found

# updating values
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})

# deleting values
del student['age']
student.pop('phone')

# reading dictionaries
print(len(student))
print(student.keys())
print(student.values())
print(student.items())

# using loops
for key in student:
    print(key)
for key, value in student.items():
    print(key, value)
