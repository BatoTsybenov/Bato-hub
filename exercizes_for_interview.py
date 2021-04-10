
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
