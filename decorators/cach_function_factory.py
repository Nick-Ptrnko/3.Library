'''
Мені потрібно замикати результати виконання функції в моєму декораторі.
Є проста функція яка додає два числа а та б. Потрібно замкнути змінні передані цього разу в функцію,
так щоб наступного разу викликаючи цю функцію з цими ж змінними не проводити розрахунки повторно.
Я хотів би дослідити скільки я таким чином можу зберігати результатів у фунції. Чи може це бути ніби
записником.
'''
def decorator():
    def inner(func):
        cache = {}
        # Зауваження: `nonlocal cache` тут не потрібен, 
        # оскільки ви змінюєте вміст словника, а не сам об'єкт `cache`.
        
        def wrapper(a1, b1):
            key = (a1, b1) # Створюємо ключ
            
            if key in cache:
                # 1. Cache Hit: Беремо з кешу і повертаємо.
                result = cache[key]
                print(f"Отримано з кешу: {result}\n Кеш зараз: {cache}")
            else:
                # 2. Cache Miss: Обчислюємо лише один раз.
                result = func(a1, b1) 
                cache[key] = result # Зберігаємо в кеш
                print(f"Обчислено новий результат: {result}\n Кеш оновлено: {cache}")
            
            return result # Повертаємо єдиний результат
            
        return wrapper
    return inner

@decorator()
def suma(a, b):
    # Додамо print, щоб бачити, коли функція справді виконується
    print(f"-> ВИКОНУЄТЬСЯ SUMA({a}, {b})")
    return a + b

# --- Тестування ---
print("--- Виклик 1 (2, 3) ---")
print("Результат:", suma(2, 3)) 

print("\n--- Виклик 2 (1, 1) ---")
print("Результат:", suma(1, 1)) 

print("\n--- Виклик 3 (2, 3) ---")
print("Результат:", suma(2, 3)) # Має спрацювати кеш!

print("\n--- Виклик 4 (2, 2) ---")
print("Результат:", suma(2, 2))
#Моя оригінальна функція, яка працює, але Gemini придумав, як її оптимізувати
'''
def decorator():
    def inner(func):
        cache = {}
        def wrapper(a1, b1):
            nonlocal cache
            if (a1, b1) in cache:
                print(f"Getting from cache...\n Cache is {cache}")
            else:
                cache[(a1, b1)] = func(a1, b1)
                print(f"Calculating new result...\n New result is {func(a1, b1)}\n New cache is {cache}")
            return func(a1, b1)
        return wrapper
    return inner

@decorator()
def suma(a, b):
    return a+b
suma(2, 3)
suma(1, 1)
suma(2, 2)
suma(5, 7)
suma(1, 1)
suma(24, 21)
suma(2, 3)
'''
