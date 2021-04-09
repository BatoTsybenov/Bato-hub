#lists
nums = list()
evens = []



odds = [1, 3, 5, 7, 9] #5 elements, list is 5
# 0.1.2.3.4.index
friends = ['jackson', 'said', 'linur', 'tyson']
first_friend = friends[0]
print(f"friends: {friends}")
print(f"first_friends: {first_friend}")
print(f"first_friends: {friends[0].title()}")
print(f"first_friends: {friends[1]}")
print(f"first_friends: {friends[2]}")
print(f"first_friends: {friends[3]}")

print(friends[-1]) # negative index (last index)
print(f"first_friends [-1]: {friends[-1]}")
print(f"first_friends [-3]: {friends[3]}")

# adding elements -
# list.append(new el.) in the end of the list
# list.insert (index, element) on the  indicated index
friends.append('Obama') # конец
print(f"New friends list: {friends}")
friends.insert(0, 'Messi') # куда хочешь
print(f"New friends list after insert: {friends}")

#reseting
friends[2] = 'mark'
print(f"New friends list after reset: {friends}")
# friends[7] = 'elon' # error, no index 7 . need to append first

#removing element
#friends.remove('mark')
#print(f"New friends list after removing Mark: {friends}")

friends.pop(4) # what is removing (inform)
print(f"New friends list after removing 4: {friends}")

removed_friends = []
removed_one = friends.pop(4)
print(removed_one)
print(f"New friends list after popping index 4: {friends}")

del friends[-1] # remove last 1
print(f"New friends list after del index -1: {friends}")

friends = [3]
print(f"New friends list after redefining: {friends}")

friends = ['jackson', 'said', 'linur', 'tyson']


# 03/07/2021 organaxing the list / sort
print("***********************************# 03/07/2021 ********************************** organaxing the list")
names = ['sasha', 'bato', 'sophia', 'rachel', 'maria']
names.sort() #ascending
print(names)
names.sort(reverse=True) #descending
print(names)

cars = ['bmv', 'audi', 'toyota', 'subaru']
sorted_cars_asc = sorted(cars)
sorted_cars_desc = sorted(cars, reverse=True)
print(f"cars: {cars}")
print(f"sorted_cars asc: {sorted_cars_asc}")
print(f"sorted_cars desc: {sorted_cars_desc}")

cars.reverse()
print(f"cars reverse: {cars}")
sorted_cars_asc2 = sorted(cars)
sorted_cars_asc2.reverse()
print(sorted_cars_asc2)


#abstract
cars = ['bmv', 'audi', 'toyota', 'subaru']
list_size = len(cars)
print(f"list_size: {list_size}")
print(len("toyota   ")) # how many elements







