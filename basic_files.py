myfile = open('myfile.txt')

# print(myfile.read())

myfile.seek(0)  # resets cusor

print(myfile.readlines())

myfile.close()

with open('myfile.txt') as new_file:
    contents = new_file.read()

# mode='r' is read only
# mode='w' is write only (will overwrite existing file or create new one
# mode='a' is append only (adds onto file)
# mode='r+' is reading and writing
# mode='w+' is writing and reading (overwrites existing file or creates new file)
