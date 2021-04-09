class User:
    login_attempts = 0

    def __init__(self):
        pass
        self.login_attempts = 0

    def increment_login_attempts(self):
        print("incrementing the value to 0...")
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("login attempts", user1.login_attempts)
user1.reset_login_attempts()
print("login attempts", user1.login_attempts)

print("good")
# wef
# erv



