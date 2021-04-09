# Exception Handling - handle situation where you expect certain type of error
filepath = "/Users/aleksandrabardymova/dev/basics/data1/students.txt"

try:
    print('trying block started....')
    with open(filepath, 'a') as students:
        print("writing to the file..")
        students.write(f"\nSergey")
    with open(filepath, 'r') as students:
        lines = students.readlines()
        print(lines)
except FileNotFoundError as err:
    print(err)
    print("Enter correct file path. check your file path")

# print(5 / 0)
try:
    num = 5/int(input('enter the bumber'))
except ZeroDivisionError as err:
    print('You can not divide by zero')
else:
    print(f"Result of this devision: {num}")
finally:
    print("I am a finally block, always executed whatever happens with try except or else block")
print("Program is completed")
