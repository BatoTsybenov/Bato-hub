print("**********************************03/12/2021***************************")
cars = ['bugatti', 'ferrari', 'tesla', 'lexus']
for car in cars[0:3]:  # slice of the list list_name[start:stop] stop is exclusive
    print(f"the car is: {car}")

for car in cars[-1:]:  # slice of the list list_name[start:stop] stop is exclusive
    print(f"the car is: {car}")  # last one

print("_____________coping and linking_____________")
cars2 = cars
print(cars)
print(cars2)
cars.append('bmw')
print(f"cars after update: {cars}")
print(f"cars after update: {cars2}")

print("_____________coping _____________")
cars3 = cars[:]  # only copy
print(cars)
print(cars3)
cars.append('toyota')
# del cars[2]
print(f"cars after update: {cars}")
print(f"cars after update: {cars3}")  # last one is not linked

# 4.10
print("********4.10********")
print(f"first 3 items in the list are: {cars[:3]}")
print(f"first 3 items in the middle are: {cars[2:5]}")
print(f"first 3 items in the list are: {cars[3:]}")

# tuples - data structures similar to list, but can not be modified (immutable)
# lists can be modified (mutable)
print("#############################################tuples************")
cars_t = ['bugatti', 'ferrari', 'tesla', 'lexus']
print(f"first value is : {cars_t[0]}")
cars[0] = 'honda'  # possible to change
# cars_t[0] = 'honda' # not possible
print(f"carsd_t tuple: {cars_t}")

cars_t = ['honda', 'ferrari', 'tesla']
print(f"carsd_t tuple: {cars_t}")
print(f"size of the tuple: {len(cars_t)}")
