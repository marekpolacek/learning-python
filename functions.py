def hello_function():
    return "hello!"
hello_function()
print(hello_function)
print(hello_function())
hello_function().upper()

# arguments
def hello_function_2(greeting):
    return f'{greeting}!'

print(hello_function_2("hi"))

# arguments
def student_info(*args,**kwargs):
    print(args) # tuple
    print(kwargs) # dictionary

student_info('math', 'art', name='john', age='22')

courses = ['math', 'art']
info = {'name':'john', 'age':'22'}
student_info(courses, info)
student_info(*courses, **info)