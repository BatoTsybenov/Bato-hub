# 03/25/2021 functions with return statement
# start get - return

def get_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


def print_formatted_name(firstname: str, lastname: str):
    name = f"{firstname.title()} {lastname.title()}"
    return name


# full_name = get_formatted_name('john', 'doe')
# print(get_formatted_name('john', 'doe'))
# print(full_name)
# #
# print_formatted_name('ali', 'tehrani')
# student = print_formatted_name('abaur', 'eskara')
# print(f"value of student is : {student}")
# print(f"value of student is : {print_formatted_name('abaur', 'eskara')}")


# getter, setter functions
def get_description_of_what_you_want_to_get():
    return


def set_desc_of_what_you_want_update():
    pass


def get_list_of_even_numbers(num: int) -> list:
    """this function returns list of even numbers up to num"""
    # nums = []
    return list(range(2, num + 1, 2))


# print(get_list_of_even_numbers(20))
# print(get_list_of_even_numbers("20"))


def get_list_of_odd_numbers(num: int) -> list:
    """this function returns list of odd numbers up to num"""
    odds = []
    return odds


def get_letter_counts(text: int) -> dict:
    """this function returns a dictionary"""
    letter_count = {}
    return letter_count


def print_usernames(users: list):
    for user in users:
        print(f"current user is: {user}")

# print_usernames(['karim', 'ronaldo', 'roger'])  # >> users = ['karim', 'ronaldo', 'roger']

def greet_users(names):
# """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)


unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print("Printing model: " + current_design)
    completed_models.append(current_design)

print("The following models have been printed:")
for completed_model in completed_models:
    print(completed_model)