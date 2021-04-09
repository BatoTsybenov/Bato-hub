# functions
def greet_user():
    """docstring, describe function"""
    print("hello!!!")

def greet_user_by_name(name):
    """
    say hello and use the name entered
    name is required parameter, user has to pass to a function
    """
    print(f"hello, {name.title()}")

# def sum_numbers(num1, num2):
#     print(f"sum of {num1} and {num2} is {num2 + num1}")
#     print(f"square of the {num2} is : {num2**2}")

greet_user() # how you call function
greet_user_by_name('ali')
greet_user_by_name('bato')
#sum_numbers()

def describe_pet(pet_name, pet= 'dog'): # optional parameter
    print(f"i have a {pet} and we call it {pet_name.title()}")

describe_pet('lazy', 'cat')
describe_pet('snoop', 'dog')
describe_pet('fluffy')
describe_pet(pet='cat', pet_name='fluffy')
describe_pet('fluffy')

def f(x):
    print(x + 10)
f(20)

def stock_price_old_new(old,new):
    if new - old > 10:
        print(f"sell the stock at {new}")
    elif new - old < 0:
        print(f"buy the stock at {new}")
    else:
        print(f"hold the stock at price {new}")

def greet_user_by_name(firstname, lastname):
    print(f"hello ")
greet_user_by_name('jane', 'don')