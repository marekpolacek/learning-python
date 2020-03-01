# escaping special characters
message = 'Bobby'
message_2 = 'Bobby\'s world'
message_3 = "Bobby's world"
message_4 = """Bobby's world
was a show in 1990s."""

# string arrays
print(len(message_4))
print(message_4[0]) # first character
print(message_4[0:5])
print(message_4[6:])

# string methods
print(message_4.lower())
print(message_4.upper())
print(message_4.count('world')) # 1 found, -1 not found
print(message_4.replace('Bobby','Billy'))

# string concatination
greeting = 'Hello'
name = 'Michael'
message_5 = greeting + ', ' + name + '!'
print(message_5)
print('{}, {}!'.format(greeting, name))
print(f'{greeting}, {name.upper()}!')

# available methods
print(dir(name))
print(help(str))
print(help(str.lower))