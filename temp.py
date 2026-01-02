def single_number(num_list: list) -> int:
    dict_pairs = {}
    for num in num_list:
        if num not in dict_pairs:
            dict_pairs[num] = 1
        else:
            del dict_pairs[num]
    return list(dict_pairs.keys())[0]

print(single_number([2,2,1]))

print(single_number([4,1,2,1,2]))
