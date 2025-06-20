def create_dictionary(*args) -> dict:
    dictionary = {}
    number = 0
    for argument in args:
        if not isinstance(argument, (list, set, dict)):
            dictionary[argument] = number
        else:
            print(f"Cannot add {argument} to the dict!")
        number += 1
    return dictionary



print(create_dictionary(7, 1, 3))
print(create_dictionary(3, [1, 2], 5))
print(create_dictionary(3, (1, 2), 5))