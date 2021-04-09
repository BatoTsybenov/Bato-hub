print("********************03/14/2021********************")
num = 20
if num >= 1 and num <= 10 : # true
    print(f"number is equal or greater than 1 and less than 10:")
else:
    print(f"number is less than 1 or greater than 10:")

# where country='UK' or country='USA'

#age = int(input('enter the visitors age: '))
age = 3
if 0 <= age <= 4:
    print("your admission cost is $0.")
elif 4 < age < 18:
    print("your admission cost is $5.")
elif 18 <= age < 140:
    print("your admission cost is $10.")
else:
    print("invalid age was entered, buy")

#age = int(input('enter the visitors age: '))
# price = 0
# if age < 4: # read first condition
#     price = 0
# elif age < 18:
#     price = 5
# elif age < 140:
#     price = 10
# else:
#     print("invalid")
# print(f"your admisiion cost is ${price}.")
#
# print("*******************5.3**********************")
# alien_color = input('enter the elien color (green/yellow/red)')
# if alien_color == 'green':
#     print(f"you just earned 5 points!!")
# elif alien_color == 'yellow':
#     print(f"you just earned 2 points!!")
# elif alien_color == 'red':
#     print(f"you just earned 10 points")
# else:
#     print("no point, sorry, take a rest")
#
# print("***********************************************")
# friends = ()
# if friends:
#     print(f" go out make some friends")
# else:
#     print("good for you, can i be your friend")

print("*****************************5.?************************")
num = int(input('Enter a number:'))
if num % 3 == 0 and num % 5 == 0:
    print("FuzzBuzz")
elif num % 3 == 0:
    print("Fuzz")
elif num % 5 == 0:
    print("Buzz")
else:
    print("sorry")

