'''
Ти полюбляєш швидку їзду. Але, щоб вибрати машину, ти спочатку повинен
відфільтрувати їх так, що серед них не буде машини з потужністю менше бажаної.
Напиши функцію powerful_cars, яка приймає число minimal_hp і список brand_cars,
де кожний елемент це список машин певного бренду, в якому кожний елемент це
словник з елементами 'name' та 'HP'. Функція повинна повертати ідентичну структуру
даних, але тільки з машинами, в яких потужність не менше minimal_hp.

Функція повинна містити тільки конструкцію return. Використовуй list comprehension
всередині іншого list comprehension.
'''
brand_cars1 = [
    [{'name': 'Ferrari_F430', 'HP': 483},
     {'name': 'Ferrari_360', 'HP': 395},
     {'name': 'Ferrari_488', 'HP': 661}],
    [{'name': 'Lamborghini_Aventador', 'HP': 690},
     {'name': 'Lamborghini_Gallardo', 'HP': 560}]
]
minimal_hp1 = 661

def powerful_cars(brand_cars: list, minimal_hp: int) -> list:
    return [[dict_cars for dict_cars in list if dict_cars['HP'] >= minimal_hp] for list in brand_cars]
print(powerful_cars(brand_cars1,minimal_hp1))


'''
ЗАДАЧКА ВІД ШІ ДЛЯ ПОСТУПОВОГО ПІДХОДУ ДО ОСНОВНОЇ ЗАДАЧІ. ПРОБЛЕМА НЕРОЗУМІННЯ МНОЮ СПИСКА В СПИСКУ

Прибрати з усіх списків числа, які менші за задане мінімальне значення.
Напиши функцію filter_numbers, яка приймає число minimal_value і список list_of_lists, де кожен
елемент — це список чисел. Функція повинна повертати ідентичну структуру даних, але тільки з
числами, які не менші за minimal_value.
Функція повинна містити тільки конструкцію return. Використовуй list comprehension всередині
іншого list comprehension.

list_of_lists1 = [
    [1, 5, 2],
    [10, 3, 7],
    [4, 9, 6]
]
minimal_value1 = 5
def filter_numbers(list_of_lists, minimal_value):
    return [[element for element in list if element >= minimal_value] for list in list_of_lists]
print(filter_numbers(list_of_lists1, minimal_value1))

РЕЗУЛЬТАТ
[5],
[10, 7],
[9, 6]
'''
