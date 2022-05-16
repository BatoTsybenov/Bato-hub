
print("***************************swap")
def swap(a, b):
    print(f"the value of a is: {a}")
    print(f"the value of b is: {b}")
    # logic here
    temp = a
    a = b
    b = temp
    print(f"the value of a is: {a}")
    print(f"the value of b is: {b}")

swap(546, 1234)

# swapping the values without using a variable
print("___________________________________")
num1 = 'number one'
num2 = 'number two'
print(num1,"---",  num2)
num1, num2 = num2, num1
print(num1,"---",  num2)

print("******************count each letter in nay phrase*********")
def get_letter_counts(text: str) -> dict:
    """
    This function returns a dictionary with letters as keys and counts as values
    """
    letter_count = {}
    # - loop through the text
    # - create a dictionary for this letters
    # - add each letter to the dictionary as a key and count (starting from 0) as a value
    # - every time you add a letter to a dictionary check if dictionary has the same key, if dictionary has a key you increment the valeu
    # if dictionary does not have you create new element and value = 1
    # a: 1+1, d: 1+1, e: 1
    return letter_count

# exercises:
# 1. FuzzBuzz, assume user enter the integer number>0
#   print Fuzz if the number is dividable by 3
#   print Buzz if the number is dividable by 5
#   print FuzzBuzz if the number is dividable by 3 and 5
# % - modulus - operator to return remainder in division
# // - floor division - division ignoring the remainder and considering only dividable num
# num % 5 == 0 - calculates num%5 and returns a remainder, and that remainder is compared to 0, which means if remainder is 0 num is devidable by 5 without any remainder.


num = int(input("enter the number > 0 :"))
if (num % 3 == 0) and (num % 5 == 0):
    print(f"FuzzBuzz your number {num} dividable by 3 and 5")
elif num % 3 == 0:
    print(f"Fuzz your number {num} dividable by 3")
elif num % 5 == 0:
    print(f"Buzz your number {num} dividable by 5")

number = int(input("Enter a number: "))
if number % 3 == 0 and number % 5 != 0:
    print ("Fuzz")
elif number % 5 == 0 and number % 3 != 0:
    print("Buzz")
elif number % 3 == 0 and number % 5 == 0:
    print("FuzzBuzz")

# H/w:
# # Implement sum() with for loop
# Double characters in a string (e.g. “abc” => “aabbcc”)
# for letter in "hello":
#     print(letter)
# # Prove that a number is a prime
# # Prove that a string is a palindrome (mom, dad, madam, kayak etc)
# #


# Exercise 5-10
current_users = ['mary', 'stanley', 'joseph', 'jennifer', 'Admin']
new_users = ['sam', 'stanley', 'Mathew', 'mia', 'jennifer']
current_users_lower =[user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")

# H/W:
# 9-5. Login Attempts: Add an attribute called login_attempts to your User
# class from Exercise 9-3 (page 166). Write a method called increment_
# login_attempts() that increments the value of login_attempts by 1. Write
# another method called reset_login_attempts() that resets the value of login_attempts to 0.
# Make an instance of the User class and call increment_login_attempts()
# several times. Print the value of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print login_attempts again to
# make sure it was reset to 0.
class User:
    login_attempts = 0

    def __init__(self):
        pass
        self.login_attempts = 0

    def increment_login_attempts(self):
        print("incrementing the value to 0...")
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("login attempts", user1.login_attempts)
user1.reset_login_attempts()
print("login attempts", user1.login_attempts)

print("good")

print("*************************9.1****************")
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} the best place if "
              f"you are looking for {self.cuisine_type} cuisine!")

    def open_restaurant(self):
        print(f"{self.restaurant_name} restaurant is open!")


my_res = Restaurant("'Hello'", "russian")
print(my_res.restaurant_name)
print(my_res.cuisine_type)
my_res.describe_restaurant()
my_res.open_restaurant()

print("*************************9.2****************")
class Restaurant():
    """Restaurant should store two attributes: a restaurant_name and a cuisine_type."""

    def __init__(self, name, cuisine):
        self.name = name.title()
        self.cuisine = cuisine.title()

    def describe_restaurant(self):
        message = f"{self.name} serves wonderful {self.cuisine} ."
        print(f"\n{message}")

    def open_restaurant(self):
        message = f"{self.name} is now open!"
        print(f"\n{message}")


restaurant = Restaurant('Luigi', 'pizza')
restaurant.describe_restaurant()

applebees = Restaurant("applebees", 'salmon')
applebees.describe_restaurant()

captain_louies = Restaurant('captain louies', 'lobsters')
captain_louies.describe_restaurant()

print("*************************9.3****************")

class User:
    def __init__(self, first_name, last_name, occupation, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.address = address
        self.phone = phone

    def describe_user(self):
        """print summary of user info"""
        print(f"\t{self.first_name.title()}")
        print(f"\t{self.last_name.title()}")
        print(self.occupation)
        print(self.address)
        print(self.phone)


    def greet_user(self):
        """Print personalized greeting to a user"""
        print(f"Hello {self.first_name.title()}, nice to see you!")


# create several instances, and use both methods for each:
person1 = User("tom", "jefferson", "programmer", "NYC", "212-0000")
person2 = User("george", "jefferson", "programmer", "NYC", "212-0000")
person3 = User("jessica", "thomson", "programmer", "NYC", "212-0000")

person1.describe_user()
person2.describe_user()
person3.describe_user()

person1.greet_user()
person2.greet_user()
person3.greet_user()

print("*************************9.4*************************")


