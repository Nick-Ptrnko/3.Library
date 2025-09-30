'''
Дана функція send_secure_information, яка приймає словник user, вона повідомляє користувачу
деяку секретну інформацію.
Напиши декоратор admin_required, який перевіряє атрибут user'a 'is_admin'
і якщо він False - виводить повідомлення з забороною, як показано у прикладі.
'''
from typing import Callable


def admin_required(func: Callable) -> None:
    def inner(dic: dict):
        if dic['is_admin']:
            func(dic)
        else:
            print("You are not allowed to see this information!")
    return inner

@admin_required
def send_secure_information(user: dict) -> None:
    print(f"{user['name']}, site's secure code is 'SecUR43Esit78Eco90DE'")

send_secure_information({'name': 'Administrator', 'is_admin': True})
# Administrator, site's secure code is 'SecUR43Esit78Eco90DE'

send_secure_information({'name': 'User1234', 'is_admin': False})
# You are not allowed to see this information!


