# Dictionary - java (hashmap, hashtable) 03/18/2021

# key/value
# create, access, modify (add, remove, update el)
# looping
# builtin functions

# create!!!!!
my_friend = {}
my_house = dict()
my_car = {"brand": "Ford", "model": "Mustang", "year": 1964, 1: 'value of 1'}

print(my_car)
print(my_car['brand'])
print(f"the value of key 'brand' is : {my_car['brand']}")
print(my_car[1])

# add
my_car['price'] = 125000.00
print("price is added-----------")
print(my_car)

#  update
print("price is updated")
my_car['price'] = 120000.00
print(my_car)

# removing values from dictionary
print("element with key 1 is being removed")
del my_car[1]
print(my_car)


