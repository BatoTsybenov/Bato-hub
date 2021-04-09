# 03/11/2021 list (con tinue)
cars = ['bmw', 'audi', 'toyota', 'subaru']

# making numerical list

nums = range(4)
print(nums)
nums2 = list(range(4))
print(nums2)

# shift fn +f6 - shortcut for refactor > rename

for num in range(4, 8):
    print(f"range start and stop: {num}")
for num in range(1, 9, 3):  # start ,stop ,interval between
    print(num)

evens = []
print("print all even numbers from 1-16")
for num in range(0, 17, 2):
    print(num)
    evens.append(num)
    print(evens)
print(F" final loop: {evens}")

print("print the squares of numbers from 10 to 20")
for num in range(10, 21):
    print(num ** 2)  # squares

squares = list()
for num in range(10, 21):
    squares.append(num ** 2)
print(squares)
print(min(squares))  # min
print(max(squares))  # max
print(sum(squares))  # sum

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars_len = len(cars)
for car in cars:
    print(car)
    print(f"index of the {car} is {cars.index(car)}")

# looping the list using index
for ind in range(len(cars)):
    print(ind)
    print(f"index of the {cars[ind]} is {ind}")

# -----------------------------------------------------------------
print("list comprehension")
squares = list()
for num in range(10, 21):
    squares.append(num ** 2)

squares = [num ** 2 for num in range(10, 21)]
print(squares)

print("**********************************03/12/2021***************************")