# https://www.youtube.com/watch?v=NIWwJbo-9_8&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7&index=20
# error handling

# general exceptions
try:
    file = open('non_existing_file.txt')
except Exception:
    print('No such file.')

# specific exceptions
try:
    file = open('non_existing_file.txt')
except FileNotFoundError as e:
    print('No such file. ', e)
except Exception as e:
    print('Something went wrong. ', e)

# else clause
try:
    file = open('file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()

# finally clause
try:
    file = open('file.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(file.read())
    file.close()
finally:
    print('final block')

# raising custom exceptions
try:
    file = open('file.txt')
    if file.name == 'file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('custom exception')
else:
    print(file.read())