
#      ПЕРШЕ ВИРІШЕННЯ ЗАДАЧІ ЧЕРЕЗ ЛІЧИЛЬНИК В ЦИКЛІ ТА ІТЕРАЦІЮ ПО СЛОВНИКАМ (8 РЯДКІВ)
'''
def get_outdated(robots: list, new_version: int) -> list:
    to_update = []
    number = 0
    for robot in robots:
        if robot["core_version"] < new_version:
            to_update.append(number)
        number += 1
    return to_update
'''

#       ДРУГЕ ВИРІШЕННЯ ЗАДАЧІ ЧЕРЕЗ ІТЕРАЦІЮ ПО RANGE. ІНДЕКС СЛОВНИКА ТА КЛЮЧ (6 РЯДКІВ)
'''
def get_outdated(robots, new_vers):
    outdated = []
    for robot in range(len(robots)):
        if robots[robot]["core_version"] < new_vers:
            outdated.append(robot)
    return outdated
'''

robots1 = [
  { "core_version": 9 },
  { "core_version": 13 },
  { "core_version": 16 },
  { "core_version": 9 },
  { "core_version": 14 },
]


#                ТРЕТЄ ВІРІШЕННЯ ЗАДАЧІ ЧЕРЕЗ List Comprehension

def get_outdated(robots, new_vers):
    return [robot for robot in range(len(robots)) if robots[robot]["core_version"] < new_vers]

print(get_outdated(robots1, 8))

'''
result = [expression for element in iterable]
Where:
- `iterable` is an object we iterate over;
- `element` is a value from `iterable` in every step;
- `expression` is a modified element from `iterable` objects, which will be written to the `result` list;
- `result` is a newly created list.

List comprehension provides an opportunity (можливість) to specify a condition for the elements which have to be included in a new list:

result_1 = [expression for element in iterable if condition]

Where:
- `condition` is a condition under which the value to the list will be written;
- `default_expression` is the value that will be written to the list if the `condition` is not met.
'''

#       ТУТ ВИДАЄТЬСЯ НЕ СПИСОК, А ЗНАЧЕННЯ ЗАСТАРІЛИХ РОБОТІВ
'''
def get_outdated(robots: list, new_version: int) -> list:
    return [robot["core_version"] for robot in robots if robot["core_version"] < new_version]
'''
#       ІТЕРАЦІЯ ПО ДВОМ ЗМІННІМ
'''
def get_outdated(robots: list, new_version: int) -> list:
    return [index for index, robot in enumerate(robots) if robot["core_version"] < new_version]
'''


#           ДОВІДКА ПО ФУНКЦІЇ enumerate
'''
languages = ['Python', 'Java', 'JavaScript']
enumerate_languages = enumerate(languages)
# Конвертуємо перелічувальний об'єкт в список
print(list(enumerate_languages))
[(0, 'Python'), (1, 'Java'), (2, 'JavaScript')]
'''