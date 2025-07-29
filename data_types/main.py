print("Гід по змінним в Python")

def get_str_value():
    return input("Введіть рядок тексту (наприклад, Привіт): ")

def get_set_value():
    print("Введіть елементи множини, розділені комами (наприклад, 1,2,3):")
    return set(input("Ваша множина: ").split(','))

def get_tuple_value():
    print("Введіть елементи кортежу, розділені комами (наприклад, 1,2,3):")
    return tuple(input("Ваш кортеж: ").split(','))

def get_float_value():
    while True:
        user_input = input("Введіть число з плаваючою комою (наприклад, 3.14): ")
        try:
            return float(user_input)
        except ValueError:
            print(f"Помилка: '{user_input}' не є коректним числом з плаваючою комою. Спробуйте ще раз.")

# Словник для зручного доступу до функцій обробки типів
type_handlers = {
    '1': ('str', get_str_value),
    '2': ('set', get_set_value),
    '3': ('tuple', get_tuple_value),
    '4': ('float', get_float_value),
}

while True:
    print("\nВиберіть значення:")
    print(" 1) str")
    print(" 2) set")
    print(" 3) tuple")
    print(" 4) float")
    print(" 0) Вийти")

    selected_type = input("Ваш вибір (0-4): ")

    if selected_type == '0':
        print("Дякую за використання гіда!")
        break

    if selected_type in type_handlers:
        type_name, handler_func = type_handlers[selected_type]
        print(f"Ви обрали {selected_type}) це тип '{type_name}'")
        try:
            user_value = handler_func()
            print(f"Ви ввели значення: {user_value}")
            print(f"Тип змінної: {type(user_value)}")
        except Exception as e:
            print(f"Виникла непередбачена помилка при обробці типу '{type_name}': {e}")
    else:
        print("Будь ласка, оберіть пункт від 0 до 4.")


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
