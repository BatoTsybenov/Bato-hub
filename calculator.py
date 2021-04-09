what = input("What we do (+, -): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if what == "+":
    c = a + b
    print("result: " + str(c))
if what == "-":
    c = a - b
    print("result: " + str(c))
else:
    print("Mission is not completed")
