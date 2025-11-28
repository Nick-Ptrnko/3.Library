"""
Ти обслуговуєш програмне забезпечення атомної електростанції. Дуже важливо, щоб пристрої відгукувалися якнайшвидше
після натискання клавіші на панелі керування.
Максимальний час відгуку пристрою до 50 мілісекунд включно вважається допустимим.
Напиши такі винятки:

SlowResponse - виняток, який буде викликатися, якщо час відгуку у межах 51 і 75 мілісекунд,
його метод __init__ приймає ім'я пристрою та час відгуку та видає таке повідомлення про помилку:
raise SlowResponse(name="Pressure compensator", response=65)
# Warning! Pressure compensator has a slow response of 65 ms.

ExtraSlowResponse - виняток, який буде викликатися якщо час відгуку у межах 76 і 100 мілісекунд,
видає таке повідомлення про помилку:
raise ExtraSlowResponse(name="Pressure compensator", response=87)
# Alarm! Pressure compensator has a very slow response of 87 ms.

DangerouslySlowResponse - виняток, який буде викликатися, якщо час відгуку більше 100 мілісекунд,
видає таке повідомлення про помилку:
raise DangerouslySlowResponse(name="Pressure compensator", response=190)
# Nuclear power station is in danger! Pressure compensator has a dangerously slow response of 190 ms.

Кожний більш серйозний виняток має наслідуватись від попереднього, а SlowResponse має наслідуватись
від Exception.
Напиши функцію check_device_response, яка перевіряє час відгуку пристрою. Вона приймає словник device з ім'ям
та максимальним часом відгуку, ця функція повинна викликати відповідний виняток, якщо час відгуку вищий за норму.
check_device_response(device={"name": "Polar crane", "response": 52})
# SlowResponse: Warning! Polar crane has a slow response of 52 ms.

Напиши функцію check_station_devices, яка перевіряє список пристроїв. Вона приймає список із пристроями і
для кожного пристрою викликає функцію check_device_response. Ця функція повинна обробляти можливі винятки,
виводити повідомлення з помилкою та додавати до нього додаткове повідомлення:
check_station_devices([
  {"name": "Polar crane", "response": 52},
  {"name": "Reactor shaft", "response": 81},
  {"name": "Pressure compensator", "response": 149},
  {"name": "Steam generator", "response": 40},
])
# Warning! Polar crane has a slow response of 52 ms. Pay attention!
# Alarm! Reactor shaft has a very slow response of 81 ms. Needs to be repaired!
# Nuclear power station is in danger! Pressure compensator has a dangerously slow response of 149 ms. We are in serious trouble!

"""
class SlowResponse(Exception):

    def __init__(self, name: str, response: int, message=None) -> None:
        self.name = name
        self.response = response
        if message is None:
            message = f"Warning! {self.name} has a slow response of {self.response} ms."
        super().__init__(message)

#raise SlowResponse(name="Pressure compensator", response=65)
class ExtraSlowResponse(SlowResponse):

    def __init__(self, name: str, response: int, message=None) -> None:
        self.name = name
        self.response = response
        if message is None:
            message = f"Alarm! {self.name} has a very slow response of {self.response} ms."
        super().__init__(name, response, message)

#raise ExtraSlowResponse(name="Pressure compensator", response=87)
class DangerouslySlowResponse(ExtraSlowResponse):

    def __init__(self, name: str, response: int) -> None:
        self.name = name
        self.response = response
        danger_message = f"Nuclear power station is in danger! {self.name} has a dangerously slow response of {self.response} ms."
        super().__init__(name, response, message=danger_message)


#raise DangerouslySlowResponse(name="Pressure compensator", response=190)

def check_device_response(device: dict) -> None:
    if 51 <= device["response"] <= 75:
        raise SlowResponse(name=device["name"], response=device["response"])
    elif 76 <= device["response"] <= 100:
        raise ExtraSlowResponse(name=device["name"], response=device["response"])
    elif device["response"] > 100:
        raise DangerouslySlowResponse(name=device["name"], response=device["response"])

check_device_response(device={"name": "Polar crane", "response": 120})
