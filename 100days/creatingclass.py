class User:

    def __init__(self, username, user_id):
        print("creating user...")
        self.id = user_id
        self.username = username
        print(f"created {username}")
        self.following = 0
        self.followers = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_01 = User("vaishaal", "001")
user_02 = User("krishna", "002")

user_01.follow(user_02)

print(user_01.followers)
print(user_02.followers)
print(user_01.following)
print(user_02.following)
