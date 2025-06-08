"""Query the name and write it to file"""
FILENAME = 'name.txt'
name = input("Name: ")
in_file = open('name.txt', 'w',)
print(name, file=in_file)
in_file.close()

#2.
"""Opening the file and reading the name for output"""
in_file = open('name.txt', 'r')
name = in_file.read().strip()
in_file.close()