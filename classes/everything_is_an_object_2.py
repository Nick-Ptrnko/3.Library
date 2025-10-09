class Friend:
    def __init__(self, name):
        self.name = name

friend = Friend("John")
print(friend.name)

guest = friend

guest.name = "Sherlock"
print(friend.name)

guest = None
print(friend.name)
