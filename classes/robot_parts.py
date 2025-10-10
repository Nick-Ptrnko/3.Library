"""
Є клас Robot, його метод __init__ приймає кількість частин із яких він виготовляється:
wheels, gears, pistons і зберігає їх у властивостях відповідно.
Напиши функцію robots_parts, яка приймає список з екземплярами класу Robot, підраховує суму частин різного виду,
записує її в словник з ключами 'wheels', 'gears', 'pistons' та повертає його.
Приклад:


robots_parts(robots) == {
  'wheels': 36,
  'gears': 43,
  'pistons': 54
}
"""
class Robot:
    def __init__(self, wheels: int, gears: int, pistons: int) -> None:
        self.wheels = wheels
        self.gears = gears
        self.pistons = pistons


def robots_parts(robots: list) -> dict:
    parts = {"wheels": 0, "gears": 0, "pistons": 0}
    for robot in robots:
        parts["wheels"] += robot.wheels
        parts["gears"] += robot.gears
        parts["pistons"] += robot.pistons
    return parts

robots = [
  Robot(wheels=10, gears=18, pistons=16),
  Robot(wheels=4, gears=8, pistons=8),
  Robot(wheels=22, gears=17, pistons=30),
]

print(robots_parts(robots))
