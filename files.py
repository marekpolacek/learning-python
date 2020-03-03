# open the file for reading
f = open('file.txt')
f.close()

f = open('file.txt', 'r') # read
print(f.name)
print(f.mode)
print(f.encoding)
f.close()

f = open('file.txt', 'w') # write
f.close()
f = open('file.txt', 'a') # append
f.close()
f = open('file.txt', 'r+') # read write
f.close()

# opening file using a context manager
with open('file.txt', 'r') as f:
    print(f.name)
    print(f.mode)
    print(f.encoding)
    content_read = f.read()
    content_readlines = f.readlines() # list of lines
    content_readline = f.readline() # one line per call
print(f.closed)

print(content_read)
print(content_readlines)
print(content_readline)

with open('file.txt', 'r') as f:
    for line in f:
        print(line, end='')

with open('file.txt', 'r') as f:
    content = f.read(100)
    print(content, end='')

with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file.txt", "r") as file:
    batch_size = 10
    contents = file.read(batch_size)
    while len(contents) > 0:
        print(contents, end='*')
        contents = file.read(batch_size)

with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file.txt", "r") as file:
    batch_size = 10
    contents = file.read(batch_size)
    print(contents, end='')
    # print(file.tell()) # gets the current position
    print(file.seek(0))
    contents = file.read(batch_size)
    print(contents, end='')
    print(file.seek(20))
    contents = file.read(batch_size)
    print(contents, end='')

with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file.txt", "w") as file:
    file.write('No bees')

with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file.txt", "r") as file:
    print(file.read())

# copying files
with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file.txt", "r") as file_read:
    with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\file_write.txt", "w") as file_write:
        for line in file_read:
            file_write.write(line)

# working with binary files
with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\picture.jpg", "rb") as file_read:
    with open("C:\\Users\\one-mapo\\PycharmProjects\\learning-python\\picture_copy.jpg", "wb") as file_write:
        chunk_size = 4096
        file_chunk = file_read.read(chunk_size)
        while len(file_chunk) > 0:
            file_write.write(file_chunk)
            file_chunk = file_read.read(chunk_size)
