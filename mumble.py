def mumbling(string: str) -> str:
    new_string = ""
    for i, char in enumerate(string, start=1):
        new_string += char.upper() + char.lower() * (i - 1) + "-"
    return new_string[0:-1]

print(mumbling("abcd"))
print(mumbling("RqaEzty"))