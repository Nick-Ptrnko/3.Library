#################               Prime numbers           #######################
'''
Напиши функцію prime_numbers, яка приймає список чисел numbers і повертає словник, який показує які числа є простими.
Тобі вже дана функція is_prime, яка перевіряє чи число просте. Використовуй її.
Функція повинна містити тільки конструкцію return. Використовуй dict comprehension.
Приклад:
numbers1 = [19]
prime_numbers(numbers) == {19: True}
numbers2 = [3, 6, 12, 17]
prime_numbers(numbers) == {3: True, 6: False, 12: False, 17: True}
'''
#                          РОЗВ'ЯЗОК
'''
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

numbers1 = [19]
numbers2 = [3, 6, 12, 17]
def prime_numbers(numbers: list) -> dict:
    return {number: is_prime(number) for number in numbers}

print(prime_numbers(numbers1))
'''

####################           Get users data    ##########################
'''
Тобі приходять дані про користувачів твоєї компанії. Але ці дані не впорядковані і, щоб
полегшити роботу своїх колег,
тобі треба їх структурувати. Було б не погано мати таку структуру даних, в якій ти можеш
отримати інформацію про користувача, звертаючись за id цього користувача.

Напиши функцію get_users_data, яка отримує список з даними користувачів.
Список з даними користувачів це список, який складається з кортежів, кожний з яких
складається з
чотирьох значень: id, username, email, password конкретного користувача.

Функція повинна повертати словник, в якому ключі це id користувача, а значення цих ключів -
також словник з рештою даних: username, email, password.
Функція повинна містити тільки інструкцію return. Використовуй dict comprehension.

Приклад:
users1 = [
          (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge')
        ] # Тільки один користувач
get_users_data(users) == {
    12: {
          'username': 'Maxim',
          'email': 'maxim@example.com',
          'password': 'UBg11eub42hge'
        },
}  # В результаті словник з одним ключем - id користувача


users2 = [
            (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge'),
            (13, 'Dmitro', 'dmitro@example.com', 'sdTioT36723fw'),
            (14, 'Roman', 'roman@example.com', 'hbFEkj34NggE2'),
            (15, 'Ivan', 'ivan@example.com', 'sdTioT36723fw'),
        ] # Чотири користувачі

get_users_data(users) == {
    12: {'username': 'Maxim', 'email': 'maxim@example.com', 'password': 'UBg11eub42hge'},
    13: {'username': 'Dmitro', 'email': 'dmitro@example.com', 'password': 'sdTioT36723fw'},
    14: {'username': 'Roman', 'email': 'roman@example.com', 'password': 'hbFEkj34NggE2'},
    15: {'username': 'Ivan', 'email': 'ivan@example.com', 'password': 'sdTioT36723fw'},
} # В результаті словник з чотирьма ключами - id користувачів

'''
#                          РОЗВ'ЯЗОК
users1 = [
          (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge')
        ]

users2 = [
            (12, 'Maxim', 'maxim@example.com', 'UBg11eub42hge'),
            (13, 'Dmitro', 'dmitro@example.com', 'sdTioT36723fw'),
            (14, 'Roman', 'roman@example.com', 'hbFEkj34NggE2'),
            (15, 'Ivan', 'ivan@example.com', 'sdTioT36723fw'),
        ]

def get_users_data(users: list) -> dict:
    return {user[0]: {'username': user[1], 'email': user[2], 'password': user[3]} for user in users}

print(get_users_data(users2))