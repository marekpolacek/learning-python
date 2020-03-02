# import my_module
# my_module.function()

# import my_module as mm
# mm.function()

# from my_module import function
# function()

# from my_module import function as f, function_2
# f(test)

# from my_module import *
# f(test)

# system directories to lookup modules
import sys
print(sys.path)

# add custom location to lookup modules
#sys.path.append('C:\\Users\\one-mapo\\Desktop\\my_module')

import random
courses = ['history', 'math', 'physics', 'compsci']
random_course = random.choice(courses)
print(random_course)

import math
radians = math.radians(90)
print(radians)
print(math.sin(radians))

import datetime
today = datetime.date.today()

import calendar
print(calendar.isleap(2020))

import os
print(os.getcwd())
print(os.__file__)

import antigravity
