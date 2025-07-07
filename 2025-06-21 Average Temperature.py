'''
Ти завжди мріяв відвідати Париж, але, щоб вибрати в якому місяці ти туди відправишся,
ти повинен бути впевнений, що середня температура в цьому місяці не буде нижче бажаної.
Напиши функцію average_temperature, яка приймає словник months з місяцями і середньою
температурою та число temperature. Ця функція повинна повернути словник з місяцями,
середня температура яких більша за temperature.
Функція повинна містити тільки інструкцію return. Використовуй dict comprehension.
Приклад:
months1 = {'Dec': -4.9, 'Jan': -2.2, 'Feb': 2.1}
temperature1 = 5
average_temperature(months, temperature) == {}
# Нема місяців з середньою температурою більше 5

months2 = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
temperature = 20
average_temperature(months, temperature) == {'Jul': 23.8, 'Aug': 22.9}
# Два місяці з середньою температурою більше 20


If you have a dict and want to iterate over it in the same way as using the `.items()` method
— you can use such syntax:
result = {key: value for key, value in dictionary.items()}
'''

months2 = {'Jun': 18, 'Jul': 23.8, 'Aug': 22.9}
temperature2 = 10
months1 = {'Dec': -4.9, 'Jan': -2.2, 'Feb': 2.1}
temperature1 = 5
months3 = {'Nov': 3.7, 'Oct': 9.2, 'Sep': 16}
temperature3 = 12
def average_temperature(months: dict, temperature: int) -> dict:
    return {month: avrg_temp for month, avrg_temp in months.items() if avrg_temp > temperature}


print(average_temperature(months3, temperature3))
print(average_temperature(months2, temperature2))
