def create_dict(keys_tuple: tuple) -> dict:
    result_dict = {}
    for index, key in enumerate(keys_tuple):
        try:
            result_dict[key] = index
        except TypeError:
            print(f"Cannot add {key} to the dict!")
    return result_dict


#dictionary = create_dict((7, 1, 3))
dictionary = create_dict((None, [1, 2], 5))
print(dictionary)