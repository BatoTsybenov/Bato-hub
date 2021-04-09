print("*********************8.2************************")
def favorite_book(title):
    print(f"one of my favorite book is '{   title.upper()   }'")


favorite_book('magic')

def multi_num(a:int, b:int):
    c = a*b
    print(f"product of {a} and {b} is {c}")


multi_num(3,6)
multi_num(0,6)
multi_num(True, True)
# multi_num(5, )
""""
def public_void_multi_num(int a, int b)
    {
    int c = a*b
    print(f"product of {a} and {b} is {c}")
    }
"""
def favorite_book(title:str):
    print(f"one of my favorite book is '{title.upper()}'")

def test_function(par1: str):
    print(f"")

# swapping values without using third a variable
# a, b = b, a
print("**************************************************")
num1 = 'number one'
num2 = 'number two'
# num1, num2 = num2, num1
print(num1, num2)
print(num2, num1)
