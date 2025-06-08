# filename = input("filename: ")
# file = open(filename, 'r')
# for line in file:
#     if line.startswith("#"):
#         print(line)
# file.close()

#
# filename = 'name.txt'
# name = input("Name: ")
# with open(filename, 'w') as out_file:
#     print(name, file=out_file)
# print("Done")


s = "\tPython, Monty \n"
print(s[1], ".", sep="")
print(s.strip(), ".", sep="")
s.replace(' ', '*')
print(s.lstrip(), ".", sep="")
print(s.strip().split(','))