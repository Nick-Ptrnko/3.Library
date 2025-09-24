'''
У тебе є функція create_permissions, яка отримує список словників з користувачами та виводить повідомлення про створені дозволи.
Твоя задача: напиши такий декоратор only_admin, який бере перший аргумент users, переданий в функцію, і потім фільтрує
тільки тих користувачів, у кого is_admin = True, і тільки для таких користувачів викликає функцію, яку він декорує.
Зверни увагу: поле is_admin може бути не тільки типу bool.
Приклад:
create_permissions(users)
# Creating permissions for admin
# Creating permissions for moderator_a11
# Creating permissions for admin_2nd
'''
users = [
     {'username': 'admin', 'is_admin': True},
     {'username': 'moderator_a11', 'is_admin': True},
     {'username': 'custom_user1', 'is_admin': False},
     {'username': 'custom_user2', 'is_admin': False},
     {'username': 'admin_2nd', 'is_admin': True},
]

def only_admin(func):
    def wrapper(lst: list):
        lst2 = []
        for user in lst:
            if user.get("is_admin") is True:
                lst2.append(user)
        func(lst2)
    return wrapper

@only_admin
def create_permissions(users: list) -> None:
    for user in users:
        print(f'Creating permissions for {user["username"]}')

create_permissions(users)