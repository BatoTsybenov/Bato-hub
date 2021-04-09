# list of lists
# list in dictionary
# dictionary in dictionary

print("*********************list of lists***********************")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = [companies, cities, countries]
print(customers) # print list
print(customers[0])
print(customers[0][0])
print(f"printing barcelona: {customers[1][2]}") # printing barc

multi_dim_nums = [
    [3, 9, 0],
    [2, 7, 1],
    [0, 1, 1]]

print(f"printing 7: {multi_dim_nums[1][1]}")

print("Nested looping through multidimensional list(array)")
for column in customers:
    print(column)
   # ['level up', 'abc company', 'ola company']
    for value in column:
        print(value.upper())
for city in customers[1]:
    print(city, end='\t')

# h/w print multiplication table
# num = 10
# for n in range (1, 11):
#     print(num, 'x', n, '=', num*n
print("***************** list of dictionaries**************")
user_0 = {'name': 'john', 'age': '25', 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': '20', 'city': 'paris'}
user_2 = {'name': 'mark', 'age': '35', 'city': 'tokyo'}

users = [user_1, user_0, user_2]
print(users[0])
print(users[2]['name'])
print(users[2]['age'])
print(users[2]['city'])

print("-----------looping------------")
for user in users:
    print(user['name'], end='||')
    print(user['age'], end='||')
    print(user['city'])

print("-------------------list in a dictionary-------------")
countries = ['usa', 'russia', 'spain']
cities = ['new york', 'moscow', 'barcelona']
companies = ['level up', 'abc company', 'ola company']

customers = {
    'countries': ['usa', 'russia', 'spain'],
    'cities': ['new york', 'moscow', 'barcelona'],
    'companies': ['level up', 'abc company', 'ola company']}

print(customers['cities'])
print(customers['cities'][1]) #second element from cities

print("-------------------dictionary in a dictionary-------------")
user_0 = {'name': 'john', 'age': '25', 'city': 'brooklyn'}
user_1 = {'name': 'jane', 'age': '20', 'city': 'paris'}
user_2 = {'name': 'mark', 'age': '35', 'city': 'tokyo'}

users = {
'user_0': {'name': 'john', 'age': '25', 'city': 'brooklyn'},
'user_1': {'name': 'jane', 'age': '20', 'city': 'paris'},
'user_2': {'name': 'mark', 'age': '35', 'city': 'tokyo'}
}
print(users)
print(users['user_0'])
print(users['user_0']['name'])

for user in users.keys():
    print(user)
    print(users[user]['name'])

print("******************")
for username, details in users.items():
    print(username)
    #print(details['name'])
    for key, value in details.items():
        print(f"details key is: {key}")
        print(f"details value is : {value}")

# howework 6.7-12
print("*******************6.8""""""""""""""""""""")
