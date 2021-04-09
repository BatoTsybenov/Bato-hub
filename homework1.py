# 2.1 Store a message in a variable, and then print that
#    message.
msg = "Hello world"
print(msg)

# 2.2 Store a message in a variable, and print that message.
#    Then change the value of your variable to a new message, and print the new
#    message.
msg = "Hello world i am happy"
print(msg)

# 2.3 Personal Message: Store a person’s name in a variable, and print a mes-
#    sage to that person. Your message should be simple, such as, “Hello Eric,
#    would you like to learn some Python today?”
name = "Bato"
print(name + ' ' + msg)

# 2.4 Store a person’s name in a variable, and then print that per-
#    son’s name in lowercase, uppercase, and titlecase.
name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

# 2.5 Find a quote from a famous person you admire. Print the
#    quote and the name of its author. Your output should look something like the
#    following, including the quotation marks:
#            Albert Einshtein once said, "A person who never made
#			 a mistake never tried anything new"
author = "Albert Einshtein"
quote = f'\t\t\t{author} once said, "A person who never made \n\t\t\ta mistake never tried anything new"'
print(quote)

# 2.6 Repeat Exercise 2-5, but this time store the famous per-
#    son’s name in a variable called famous_person. Then compose your message
#    and store it in a new variable called message. Print your message.
famous_person = author
message = f'\t\t\t{famous_person} once said, "A person who never made \n\t\t\ta mistake never tried anything new"'
print(message)

# 2.7 Store a person’s name, and include some whitespace
#    characters at the beginning and end of the name. Make sure you use each
#    character combination, "\t" and "\n", at least once.
#    Print the name once, so the whitespace around the name is displayed.
#    Then print the name using each of the three stripping functions, lstrip(),
#    rstrip(), and strip().
name3 = "Kate"
name2 = '\n\t\t' + "John Doe" + name3 + '\t'
print(name2.lstrip())
print(name2.rstrip())
print(name2.strip())

# Write addition, subtraction, multiplication, and division
# operations that each result in the number 8. Be sure to enclose your operations
# in print statements to see the results. You should create four lines that look
print("****************************2.8***********")
num = 5
num1 = 3
num2 = 10
num3 = 2
num4 = 4
num5 = 16
print(num + num1)
print(num2 - num3)
print(num3 * num4)
print(int(num5 / num3))

# 2-9. Favorite Number: Store your favorite number in a variable. Then, using
# that variable, create a message that reveals your favorite number. Print that
# message.
print("*********************2.9***********************")
favnum = 7
print(f"my favorite number is: {favnum}")

# 2-10. Adding Comments: Choose two of the programs you’ve written, and
# add at least one comment to each. If you don’t have anything specific to write
# because your programs are too simple at this point, just add your name and
# the current date at the top of each program file. Then write one sentence
# describing what the program does.

print("*************************2.10**********************")
# this function reveals my favorite number
fav_num = 7
print(f"my fav_num number is: {fav_num}")

# 2-11. Zen of Python: Enter import this into a Python terminal session and skim
# through the additional principles.


# hpmework 3.1,3.2, 3.5, 3.6 -7

# 3-1. Names: Store the names of a few of your friends in a list called names. Print
# each person’s name by accessing each element in the list, one at a time.
print("*************************3.1**********************")
names = ['kolya', 'bair', 'china', 'jargal']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

# example 2
for name in names:
    print(name.title())

# 3-2. Greetings: Start with the list you used in Exercise 3-1, but instead of just
#
# printing each person’s name, print a message to them. The text of each mes-
# sage should be the same, but each message should be personalized with the
#
# person’s name.
print("*************************3.2**********************")
message = "best friend forever is "
print(message + names[0].title())
print(message + names[1].title())
print(message + names[2].title())
print(message + names[3].title())

# 3.3 exercise
# Think of your favorite mode of transportation, such as a
# motorcycle or a car, and make a list that stores several examples. Use your list
# to print a series of statements about these items, such as “I would like to own a
# Honda motorcycle.”

cars = ['Bughati', 'Ferrari', ' Tesla', 'bmv']
print(f"i would like to own {cars[0].title()} motorcycle.:")
print(f"i would like to own {cars[1].title()} motorcycle.:")
print(f"i would like to own {cars[2].title()} motorcycle.:")
print(f"i would like to own {cars[3].title()} motorcycle.:")

# 3.4
print("**********3 -4 ********")
friends = ['jackson', 'said', 'linur', 'tyson']
print(f"Hi {friends[0].title()}, i would like to invite you to family dinner tommorow.")
print(f"Hi {friends[1].title()}, i would like to invite you to family dinner tommorow.")
print(f"Hi {friends[2].title()}, i would like to invite you to family dinner tommorow.")
print(f"Hi {friends[3].title()}, i would like to invite you to family dinner tommorow.")

# 3-5. Changing Guest List: You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# • Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# • Print a second set of invitation messages, one for each person who is still
# in your list
print("*************************3.5**********************")
friends = ['jackson', 'said', 'linur', 'tyson']
print(f"Today {friends[3].title()} cant come to dinner")
friends[3] = 'pasha'
print(friends)
print(f" Dear {friends[0].title()} i invite to dinner")
print(f" Dear {friends[1].title()} i invite to dinner")
print(f" Dear {friends[2].title()} i invite to dinner")
print(f" Dear {friends[3].title()} i invite to dinner")

# 3-6. More Guests: You just found a bigger dinner table, so now more space is
# available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
# statement to the end of your program informing people that you found a
# bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.
print("*************************3.6 **********************")
print(f"Dear {friends[0].title()} i found bigger table for today")
print(f"Dear {friends[1].title()} i found bigger table for today")
print(f"Dear {friends[2].title()} i found bigger table for today")
print(f"Dear {friends[3].title()} i found bigger table for today")
friends.insert(0, "soloma")
friends.insert(2, "obama")
friends.append("linkoln")
print(friends)
for friend in friends:
    print(f"dear {friend.title()} i invite you to have a dinner a bigger place")

# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.
print("*************3-7********")
print(f" i can invite only 2 people for dinner")
print(friends)
friend1 = friends.pop()
print(f" dear {friend1} i cant invite you today")
friend2 = friends.pop()
print(f" dear {friend2} i cant invite you today")
friend3 = friends.pop()
print(f" dear {friend3} i cant invite you today")
friend4 = friends.pop()
print(f" dear {friend4} i cant invite you today")
friend5 = friends.pop()
print(f" dear {friend5} i cant invite you today")
print(f" dear {friends[0]} i still invite you to dinner")
print(f" dear {friends[1]} i still invite you to dinner")
del friends[0]
del friends[0]
print(friends)

# 3.8
print("*************************3.8 **********************")

places = ['dubai', 'japan', 'switzland', 'alaska', 'italia']
print(places)
places_sorted_acs = sorted(places)
places_sorted_desc = sorted(places, reverse=True)
print(f"places_sorted_asc: {places_sorted_acs}")
print(f"places_sorted_desc: {places_sorted_desc}")
print(places)
places_reversed_alph = sorted(places, reverse=True)
print(f"reversed sorted places: {places_reversed_alph}")
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

# 4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
# pizza names in a list, and then use a for loop to print the name of each pizza.
# • Modify your for loop to print a sentence using the name of the pizza
# instead of printing just the name of the pizza. For each pizza you should
# have one line of output containing a simple statement like I like pepperoni
# pizza.
# • Add a line at the end of your program, outside the for loop, that states
# how much you like pizza. The output should consist of three or more lines
# about the kinds of pizza you like and then an additional sentence, such as
# I really love pizza!
print("************************* 4.1 **********************")
pizzas = ['peperoni', 'hawaiian', 'pasta']
for pizza in pizzas:
    print(f"I like {pizza} pizza")
print("i really love pizza")

# 4-2. Animals: Think of at least three different animals that have a common char-
# acteristic. Store the names of these animals in a list, and then use a for loop to
#
# print out the name of each animal.
# • Modify your program to print a statement about each animal, such as
# A dog would make a great pet.
# • Add a line at the end of your program stating what these animals have in
# common. You could print a sentence such as Any of these animals would
# make a great pet!
print("************************* 4.2 **********************")
animals = ['dolphin', 'dog', 'horse']
for animal in animals:
    print(f"{animal} is very smart animal")
print("this animals would make a great friend")

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
# inclusive.
print("************************* 4.3 **********************")
for num in range(1, 21):
    print(num)

# 4-4. One Million: Make a list of the numbers from one to one million, and then
# use a for loop to print the numbers. (If the output is taking too long, stop it by
# pressing ctrl-C or by closing the output window.)
# print("************************* 4.4 **********************")
# nums = []
# for num in range(1, 1000001):
#    print(num)
#    nums.append(num)
# print(nums)

# 4-5. Summing a Million: Make a list of the numbers from one to one million,
# and then use min() and max() to make sure your list actually starts at one and
# ends at one million. Also, use the sum() function to see how quickly Python can
# add a million numbers.

# print("************************* 4.5 **********************")
# nums = []
# for num in range(1, 1000001):
#     nums.append(num)
# print(f"smallest: {min(nums)}")
# print(f"biggest: {max(nums)}")
# print(f"total: {sum(nums)}")

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list
# of the odd numbers from 1 to 20. Use a for loop to print each number.
print("************************* 4.6 **********************")
for num in range(1, 21, 2):
    print(num)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
# print the numbers in your list.
print("************************* 4.7 **********************")
nums = []
for num in range(3, 31, 3):
    nums.append(num)
print(nums)

# 4-8. Cubes: A number raised to the third power is called a cube. For example,
# the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
# is, the cube of each integer from 1 through 10), and use a for loop to print out
# the value of each cube.
print("************************* 4.8 **********************")
cubes = []
for num in range(1, 11):
    cubes.append(num ** 3)
    print(cubes)

# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the
# first 10 cubes.
print("************************* 4.9 **********************")
cubes = [num ** 3 for num in range(1, 11)]
print(cubes)

# 4.10
cars = ['bugatti', 'ferrari', 'tesla', 'lexus', 'bmw', 'toyota']
print("********4.10********")
print(f"first 3 items in the list are: {cars[:3]}")
print(f"first 3 items in the middle are: {cars[2:5]}")
print(f"first 3 items in the list are: {cars[3:]}")

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement
# describing each test and your prediction for the results of each test. Your code
# should look something like this:
# car = 'subaru'
# print("Is car == 'subaru'? I predict True.")
# print(car == 'subaru')
# print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')
# • Look closely at your results, and make sure you understand why each line
# evaluates to True or False.
# • Create at least 10 tests. Have at least 5 tests evaluate to True and another
# 5 tests evaluate to False.
print("************************* 5.1 **********************")
car = 'tesla'
print("is car == 'tesla'? i predict True.")
print(car == 'tesla')
print("car == 'subaru? i predict false.")
print(car == 'subaru')


# print("************************* 5.1 **********************")
# cars = ['tesla', 'bmw', 'toyota', 'honda', 'hyundai']
# for car in cars:
#     print(f"is car == {car}? i predict True.")
#     print(car == car)
#     print(f"car == 'cresta'? i predict False.")
#     print(car == 'cresta')
print("************************* 5.2 **********************")
num = 5
num1 = 3
print(f"{num} > {num1} ? i predict True")
print(num > num1)
print(f"{num} == {num1}? i predict False")
print(num == num1)
print(f"{num} < {num1}? i predict False")
print(num < num1)
print("num != num1 ? i predict True")
print(num != num1)

print("-----------------")
b = 15
a = 5
print("b > a and b + a == 20? i predict True")
print(b > a and b + a == 20)
print("b < a or b - a == 10 i predict True")
print(b < a or b - a == 10)

print("***********************")
wine = ['white', 'red', 'dry', 'rose']
print("white wine in the list? i predict True")
print('white' in wine)
print("sparkling wine in the list? i predict False")
print('sparkling' in wine)


print("**************************************************")
current_users = ['mary', 'stanley', 'joseph', 'jennifer', 'Admin']
new_users = ['sam', 'mike', 'Mathew', 'mia', 'Cassandra']
#current_users_lower =[user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in new_users:
        print("Sorry " + new_user + ", that name is taken.")
    else:
        print("Great, " + new_user + " is still available.")


print("*********************6.1***************")
amigo = {'first_name': 'Vitaly', 'last_name': 'Didkivski', 'age': '19', 'city': 'Florence'}
print(f"my friends first name is: {amigo['first_name']}     ")
print(f"my friends last name is: {amigo['last_name']}     ")
print(f"my friends is: {amigo['age']} years old")
print(f"my friends lives is: {amigo['city']}    ")

print("*********************6.2************************")
# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary. Think of a favorite
# number for each person, and store each as a value in your dictionary. Print
# each person’s name and their favorite number. For even more fun, poll a few
# friends and get some actual data for your program.
best_friend = {'Sergei': '1', 'Erdem': '69', 'Bair': '5', 'China': '25', 'Kolya': '13'}
best_friend1 = 'Sergei'
print(best_friend1)
best_friend2 = 'Erdem'
best_friend3 = 'Bair'
best_friend4 = 'China'
best_friend5 = 'Kolya'
print(f"Sergei favorite number is: {best_friend['Sergei']}")
print(f"Erdem favorite number is: {best_friend['Erdem']}")
print(f"Bair favorite number is: {best_friend['Bair']}")
print(f"China favorite number is: {best_friend['China']}")
print(f"Kokya favorite number is: {best_friend['Kolya']}")

print("*********************6.3************************")
# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# • Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
glossary = {'variables': 'assign', 'list': 'store multiple items', 'condition': 'boolean expression', 'string': 'sequence of characters', 'looping': 'used for iterating over a sequence'}
print(f"1.variables is created the moment you first \n{glossary['variables']} a value to it")
print(f"2.list are used to \n{glossary['list']} in a single variable")
print(f"3.condition is: \n{glossary['condition'].upper()}")
print(f"4.string in Python is: \n{glossary['string'].title()}")
print(f"5.looping in Python is \n{glossary['looping'].strip()} ")

#  exercises for problem solving:
#     1. How to swap 2 variable values. e.g.: a=45 b=78 >> a=78 b=45
#     2. Count the vowels ('aeuoi') in any phrase/sentence/word.
#     user enters any phrase, you return:
#     print(f"number of {vowels}'s is : {count}")
#     3. Count each letter in any phrase
#     4. Find the first mostly used letter in a phrase.
#         (max(), dictionary, add to dictionary, if the key is in the dictionary, increment)

print("*********************7.8************************")
# Make a list called sandwich_orders and fill it with the names of vari-
# ous sandwiches. Then make an empty list called finished_sandwiches. Loop
#
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.
sandwich_orders = ['burger', 'cheeseburger', 'hamburger', 'ham eg and cheese', 'tuna']
finished_sandwiches = []
print(finished_sandwiches)
for sandwich_order in sandwich_orders:
    print(f"i made your {sandwich_order} for you")
while sandwich_orders:
    current_order = sandwich_orders.pop()
    finished_sandwiches.append(current_order)
print(finished_sandwiches)
for finished_sandwiche in finished_sandwiches:
    print(f"your {finished_sandwiche} is ready")

print("*********************7.9************************")
# Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.
sandwich_orders = ['burger', 'pastrami', 'cheeseburger', 'pastrami', 'hamburger', 'ham eg and cheese', 'pastrami']
print(sandwich_orders)
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(f"deli run out of pastrami in: {sandwich_orders}")
while sandwich_orders:
        current_order = sandwich_orders.pop()
        finished_sandwiches.append(current_order)
print(finished_sandwiches)

print("*********************7.10************************")
# Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.
# prompt = "Enter the place  what is your vacation dream:"
# while True:
#     city = input(prompt)
#     if city == 'quit':
#         break
#     else:
#         print("in my vacation i had love to go" + " " + city.title() + "!")
# city = input(prompt)
# print("in my vacation i had love to go" + " " + city.title() + "!")

print("*************************** 8.3 *************************")
# Write a function called make_shirt() that accepts a size and the
# text of a message that should be printed on the shirt. The function should print
# a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the
# function a second time using keyword arguments.
def make_shirt(size, text):
    print(f"need to make a shirt, should be of size {size} and text: {text}")


make_shirt('4', 'quality is priority')
make_shirt(text='quality is priority', size='4')

print("*************************** 8.4 *************************")
def make_shirt2(size='l', text='I love python'):
    print(f"need to make a shirt, should be of size {size} and text: {text}")
make_shirt2()

print("*************************** 8.5 *************************")
# Write a function called describe_city() that accepts the name of
# a city and its country. The function should print a simple sentence, such as
# Reykjavik is in Iceland. Give the parameter for the country a default value.
# Call your function for three different cities, at least one of which is not in the
# default country.
def describe_city(city, country='USA'):
    print(f"{city} is in {country}")


describe_city('New york', 'Barak')
describe_city('Brooklyn', )
describe_city('Moscow', 'Russia')

print("***********************************problem solving****")
# exercises for problem solving:
#     1. How to swap 2 variable values. e.g.: a=45 b=78 >> a=78 b=45
#     2. Count the vowels ('aeuoi') in any phrase/sentence/word.
#     user enters any phrase, you return:
#     print(f"number of {vowels}'s is : {count}")
#     3. Count each letter in any phrase
#       loop
#       create
#       add
#     4. Find the first mostly used letter in a phrase.
#         (max(), dictionary, add to dictionary, if the key is in the dictionary, increment)

a = 45
b = 78
print("the value a : {}".format(a))
print("the value b : {}".format(b))


def swap(a, b):
    print(f"the value of a is: {a}")
    print(f"the value of a is: {b}")
    temp = a
    a = b # assigning
    b = temp
    print(f"the value of a is: {a}")
    print(f"the value of a is: {b}")

swap(546, 1234)

#8.6-8