# 03/20/2021
# looping through dictionaries
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964}

for key in my_car:
    print("_---------------------------")
    print(f"key in this iteration is : {key}")
    print(f"value in this iteration is : {my_car[key]}")

print("-------- 2.using keys-------")
for key in my_car.keys():
    print("_---------------------------")
    print(f"key in this iteration is : {key}")
    print(f"value in this iteration is : {my_car[key]}")

#if 'model' in my_car.keys():
if 'model' in my_car:
    print(f"Yes my_car desc contains model inf")


print("-------- 3.values -------")
for value in my_car.values():
    print("_---------------------------")
    print(f"value in this iteration is : {value}")
    #print(f"value in this iteration is : {my_car[value]}")

print("-------- 4.using dict.items -------")
for key, value in my_car.items():
    print("_---------------------------")
    print(f"key in this iteration is : {key}")
    print(f"value in this iteration is : {value}")

if 1964 in my_car.values():
    print(f"Yes my_car desc contains 1966 information")

print("example with sort(), sorted(list)*********")
friends = ['john', 'jane', 'bato']
print(friends)
sorted_friends = sorted(friends)
friends.sort()
print(sorted_friends)
print(friends)

print("**********************sorted list*****************************")
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby'}
for name in sorted(favorite_languages.keys()):
    print(f"{name} favorite language is {favorite_languages[name]}")

print("*************************6.5**********************************")
rivers = {'nile': 'egypt', 'tigress': 'iraq', 'amazon': 'brazil', 'mississippi': 'usa'}

for river, country in rivers.items():
    print(f" the {river.title()} runs through {country.title()}.")

# 6.6 h/w




