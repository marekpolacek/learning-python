if True:
    print('conditional was true')
else:
    print('conditional was false')

language = 'python'
if language == 'python':
    print('language is python')
elif language == 'javascript':
    print('language is javascript')
else:
    print('other language')

# and,not operators
user = 'Admin'
logged_in = True

if user =='Admin' and logged_in:
    print('Welcome')
else:
    print('Log in please')

if not logged_in:
    print('Log in please')

# object ids and is operator
a = [1,2,3]
b = [1,2,3]
print(id(a))
print(id(b))
print(a is b)

a = [1,2,3]
b = a
print(id(a))
print(id(b))
print(a is b)

# handling false, none, zero and empty objects
condition = False
if condition: print('true')
else: print('false')
condition = None
if condition: print('true')
else: print('false')
condition = 0
if condition: print('true')
else: print('false')
condition = '' or () or [] or {}
if condition: print('true')
else: print('false')