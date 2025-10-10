"""
Створи клас Robot, метод __init__ якого приймає тільки name та записує його у властивість self.name,
a властивість self.partner спочатку None.
Створи функцію pair_robots, яка приймає список з двох імен, створює для кожного екземпляр класу Robot та
додає до кожного властивість partner з посиланням на партнера (інший об'єкт). Функція повертає кортеж з роботами.
robots = [
  'Alex',
  'Tom'
]

new_robots = pair_robots(robots)

new_robots[0].name == 'Alex' # True
all([isinstance(robot, Robot) for robot in new_robots]) # True
new_robots[0].partner is new_robots[1] # True
new_robots[1].partner is new_robots[0] # True
"""
class Robot:
    def __init__(self, name: str) -> None:
        self.name = name
        self.partner = None

def pair_robots(robots: list) -> tuple:
    for robot in robots:
        robot = Robot(robot.name)