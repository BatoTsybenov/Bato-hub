# 04/04/2021 reading file

# filepath = "/Users/aleksandrabardymova/dev/basics/data/students.txt"
filepath = "/Users/aleksandrabardymova/dev/basics/data/students.txt"

# reading an entire file
with open(filepath) as students:
    contents = students.read()
    print(contents)
print("************************************")

# making in the list of lines from file
with open(filepath) as students:
    for line in students:
        print(line, end='')


print("************************************")

# making in the list of linesd froma file
# with open(filepath, 'r') as students:
#     lines = students.readlines()
#
# print(lines)
# print(lines[0])
# print(lines[-1])
# print("************************************")
# for line in lines:
#     print(lines)

print("******************** reading from file ***************")
with open(filepath, 'a') as students:
    print("writing to the file..")
    students.write(f"\nSergey")

with open(filepath, 'r') as students:
    lines = students.readlines()
    print(lines)

print("Program is completed")