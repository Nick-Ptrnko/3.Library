"""
Ти розробляєш веб-сервіс, на якому можуть реєструватися користувачі. Але, перед тим як додати їх дані
аутентифікації в базу даних, треба, щоб ім'я та пароль користувача пройшли валідацію.
Напиши функції:
username_validation - приймає username і викликає виняток InvalidUsername, якщо довжина username
менша за 4 чи більша за 15.

password_validation - приймає password1, password2 і викликає виняток PasswordMismatch, якщо password1
і password2 не рівні між собою.

user_validation - приймає реєстраційні дані користувача - словник з username, password1, password2
і валідує ці дані за допомогою функцій username_validation та password_validation. Якщо якась з цих функцій
викликає валідаційний виняток, то user_validation повинна обробити цей виняток і викликати виняток ValidationError.

db_user_creation - приймає словник user, викликає функцію user_validation і передає туди user.
Якщо user_validation викликає виняток валідації, то db_user_creation повинна обробити цей виняток і викликати
виняток DBUserCreationError. Якщо ж користувач успішно валідований - то функція виводить повідомлення
{username} is created in the database.
"""
class InvalidUsername(Exception):
    pass


class PasswordMismatch(Exception):
    pass


class ValidationError(Exception):
    pass


class DBUserCreationError(Exception):
    pass


def username_validation(username: str):
    if len(username) < 4 or len(username) > 15:
        raise InvalidUsername

username_validation(username="User")

def password_validation(password1: str, password2: str):
    if password1 != password2:
        raise PasswordMismatch

password_validation(password1="1234", password2="1234")

def user_validation(user: dict):
    try:
        username_validation(user["username"])
        password_validation(user["password1"], user["password2"])
    except (InvalidUsername, PasswordMismatch):
        raise ValidationError

'''user_validation(
  user={"username": "User",
        "password1": "124",
        "password2": "1234"}
)
# ValidationError'''

def db_user_creation(user: dict):
    try:
        user_validation(user=user)
        print(f"{user["username"]} is created in the database")
    except ValidationError:
        raise DBUserCreationError

db_user_creation(
    user={"username": "User1",
          "password1": "password",
          "password2": "password"},
)
# User1 is created in the database.

db_user_creation(
    user={"username": "UsernameUsername",
          "password1": "password",
          "password2": "password"},
)
#  DBUserCreationError
