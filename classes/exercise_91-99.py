# print("*************************9.1****************")
# class Restaurant:
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(f"{self.restaurant_name} the best place if "
#               f"you are looking for {self.cuisine_type} cuisine!")
#
#     def open_restaurant(self):
#         print(f"{self.restaurant_name} restaurant is open!")
#
#
# my_res = Restaurant("'Hello'", "russian")
# print(my_res.restaurant_name)
# print(my_res.cuisine_type)
# my_res.describe_restaurant()
# my_res.open_restaurant()
# #
# print("*************************9.2****************")
# class Restaurant():
#     """Restaurant should store two attributes: a restaurant_name and a cuisine_type."""
#
#     def __init__(self, name, cuisine):
#         self.name = name.title()
#         self.cuisine = cuisine.title()
#
#     def describe_restaurant(self):
#         print(f"\n{self.name} service wonderful {self.cuisine} .")
#
#     def open_restaurant(self):
#         print(f"\t{self.name} is now open!")
#
#
# restaurant = Restaurant('Luigi', 'pizza')
# restaurant.describe_restaurant()
#
# applebees = Restaurant("applebees", 'salmon')
# applebees.describe_restaurant()
#
# captain_louies = Restaurant('captain louies', 'lobsters')
# captain_louies.describe_restaurant()

print("*************************9.3****************")
class User:
    def __init__(self, first_name, last_name, occupation, address, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.occupation = occupation
        self.address = address
        self.phone = phone

    def describe_user(self):
        """print summary of user info"""
        print(f"\t{self.first_name.title()}")
        print(f"\t{self.last_name.title()}")
        print(self.occupation)
        print(self.address)
        print(self.phone)


    def greet_user(self):
        """Print personalized greeting to a user"""
        print(f"Hello {self.first_name.title()}, nice to see you!")


# create several instances, and use both methods for each:
person1 = User("tom", "jefferson", "programmer", "NYC", "212-0000")
person2 = User("george", "jefferson", "programmer", "NYC", "212-0000")
person3 = User("jessica", "thomson", "programmer", "NYC", "212-0000")

person1.describe_user()
person2.describe_user()
person3.describe_user()

person1.greet_user()
person2.greet_user()
person3.greet_user()
#
# class Userlog:
#     def __init__(self, first_name, last_name, country, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.country = country
#         self.age = age
#
#     def describe_user(self):
#         print(f"Meet our guest {self.first_name + ' ' + self.last_name}!"
#               f"\n{self.first_name} is {self.age} and lives in {self.country}")
#
#     def greet_user(self):
#         print(f"Welcome {self.first_name + ' ' + self.last_name}")
#
#
# class Privileges:
#     def __init__(self, privileges):
#         self.privileges = ["can add post", "can delete post", "can ban user"]
#
#     def show_privileges(self):
#         print(f"The user has following privileges: {self.privileges}")
#
#
# class Admin(Userlog):
#     def __init__(self, first_name, last_name, country, age):
#         super().__init__(first_name, last_name, country, age)
#         self.privileges = Privileges()
