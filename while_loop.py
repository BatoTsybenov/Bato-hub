# 03/21/2021 while loop
print("***************** incrementing the variable to reach upper boundary")
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("***************** decrementing the variable to reach lower boundary")
current_number = 10
while current_number >= 5:
    print(current_number)
    current_number -= 1

color = None
while color != "quit":
    print("******* game started ***********")
    color = input("Enter your color (green/yellow/red): ")
    color = color.lower().strip()
    points = 0
    if color == 'green':
        #print("Yeah, got 15 points")
        points = 15
    elif color == 'yellow':
        points = 10
    elif color == 'red':
        points = 5
    elif color != 'quit':
        print("sorry, thats not right color, looser")
    print(f"You have {points} points")
print("closing the game")

count = 0
for letter in 'hello guys':
    if letter == 'l':
        count += 1
print(f"number of l is : {count}")