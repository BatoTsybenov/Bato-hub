# if condition
# if expression:
#     code here when expression is true
# else:
#     code here when expression is false
#

# num1_str = input("enter the num1 ")
num = 0
if num in range(5):  # compairing 2 values using ==
    print("expression is true")
else:
    print("expresion is false")
print("if statement completed here")

print("--------------------------------------------------")
num = 0
if num != 0:  # compairing 2 values using ==
    print("expression is true")
else:
    print("expresion is false")
print("if statement completed here")

print("--------------------------------------------------")
msg = input("enter the number: ")

if msg.strip() != '':  # compairing 2 values using ==
    print(f"this message was entered: \n'{msg}'")
else:
    print("whitespaces was entered")

msg = input("enter the  name: ")
if msg.strip().title() == 'john doe':
    print(f"this message was entered: {msg}'")
else:
    print(msg)

print("---if statement with lists---")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
if 'tesla' in cars:
    print("yes, we have tesla in stock")
else:
    print("sorry we dont have this car")

print("---if statement with lists---")
if 'sat' in 'today':
    print("yes")
else:
    print("sorry")

print("---if statement with lists---")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars:
    if car == 'tesla':
        print(f"this is {car.upper()}")
        break  # stoped
    else:
        print(f"current car is {car.title()}")

print("exercise:--------__-----")
nums = [45, 4, 5, 6, 3, 10, 123, 346, 4, 5, 666, 5]
# print values , if  you find 5 print 'completed'
for num in nums:
    if num == 5:
        print(num, ',' 'completed')
        break
    else:
        print(num, "this is not 5")

count = 0  # how many home work
count = count + 1  # how many 5s, count +=1

nums = [45, 4, 5, 6, 3, 10, 5, 123, 346, 4, 5, 666, 5]
cnt = 0
for num in nums:
    if num == 5:
        cnt = cnt+1
print(cnt)