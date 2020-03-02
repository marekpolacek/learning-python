nums = [1,2,3,4,5]

# for loops
for num in nums:
    if num == 3:
        print('found')
        break
    print(num)
for num in nums:
    if num == 3:
        print('found')
        continue
    print(num)

# nested loops
for num in nums:
    for letter in 'abc':
        print(num, letter)

# ranges
for i in range(10): print(i)
for i in range(1,10): print(i)

# while loops
x = 0
while x < 10:
    print(x)
    x += 1