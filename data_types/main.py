print("Гід по змінним в Python")
selected_type = input(
    "Виберіть значення:\n"
    " 1) int\n"
    " 2) float\n"
    " 3) str\n"
    " 4) dict\n"
    " 5) set\n"
    " 6) list\n"
    " 7) tuple\n"
    " 8) bool\n"
    " 9) cmplx\n"
    "Ваш вибір (1-9): "
)

# Ініціалізуємо user_value перед try-except, щоб вона була визначена навіть у разі помилки
user_value = None 

if selected_type == '1':
    print(f"Ви обрали {selected_type} це тип 'Integer' - цілі числа")
    try:
        user_input = input("Введіть ціле число (наприклад, 123): ")
        user_value = int(user_input) # Змінна user_value буде визначена тут, якщо немає помилок
        print(f"Ви ввели значення: {user_value}")
        print(f"Тип змінної: {type(user_value)}")
    except ValueError:
        print(f"Помилка: '{user_input}' не є коректним цілим числом.")
        # user_value залишається None, як і було ініціалізовано
else:
    print("Будь ласка, оберіть пункт 1, щоб перевірити 'int'.")





'''
try:
    # Код, який може викликати виняток
    результат = 10 / 0  # Спроба поділити на нуль
except ZeroDivisionError:
    # Код, який виконується, якщо виникає ZeroDivisionError
    print("Помилка: Спроба ділення на нуль!")
    результат = 0
print(f"Результат: {результат}")
'''
