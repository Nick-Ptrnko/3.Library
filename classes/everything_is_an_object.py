class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User(
    name = "Mykola",
    age = 45
)

print(user.age)

user2 = user
print(user2.age)

user2.age = 789

print(user.age)
print(type(user2))
print(user2)