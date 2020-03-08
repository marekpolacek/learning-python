# https://www.youtube.com/watch?v=D3JvDWO-BY4&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=19

# sorting lists

list = [1,2,3,5,6,4]
sorted_list = sorted(list)
print(sorted_list)
print(list)

list.sort()
print(list)

sorted_list_desc = sorted(list, reverse=True)
print(sorted_list_desc)

negative_list = [-6,-5,-4,1,2,3]
sorted_negative_list = sorted(negative_list)
print(sorted_negative_list)

sorted_absolute_list = sorted(negative_list, key=abs)
print(sorted_absolute_list)

# sorting tuples
tuple = (1,3,4,5,6,2)
sorted_tuple = sorted(tuple)
print(sorted_tuple)

# sorted dictionaries
dictionary = {'name': 'marek', 'age': 33, 'job': 'architect'}
sorted_dictionary = sorted(dictionary)
print(sorted_dictionary)

# classes
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, ${})'.format(self.name, self.age, self.salary)

employee_1 = Employee('John Doe', 30, 70000)
employee_2 = Employee('Jane Doe', 30, 80000)

employee_list = [employee_1, employee_2]

def employee_sort(employee):
    return employee.name

sorted_employees = sorted(employee_list, key=employee_sort)
# alternative 1:
# sorted_employees = sorted(employee_list, key=lambda e: e.name)
# alternative 2:
# from operator import attrgetter
# sorted_employees = sorted(employee_list, key=attrgetter('name'))
print(sorted_employees)

