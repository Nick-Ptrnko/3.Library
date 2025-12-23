'''
Cat: first 15 years = 1 human year, next 9 = +1, then every 4 = +1
Dog: first 15 years = 1 human year, next 9 = +1, then every 5 = +1
'''
def get_human_age(cat_age: int, dog_age: int) -> list:
    animal_ages = [cat_age, dog_age]
    human_ages = [0, 0]
    for i, age in enumerate(animal_ages):
        if age < 15:
            human_ages[i] = 0
        elif 15 <= age < 24:
            human_ages[i] = 1
    if animal_ages[0] >= 24:
        human_ages[0] = 2 + (animal_ages[0] - 24) // 4
    if animal_ages[1] >= 24:
        human_ages[1] = 2 + (animal_ages[1] - 24) // 5
    return human_ages

'''
def t_get_human_age():
    goals_list = [
        (0, 0, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1])
    ]
    for i in goals_list:
        result = get_human_age(i[0], i[1])
        assert result == i[2]


t_get_human_age()
'''
print(get_human_age('15', '15'))