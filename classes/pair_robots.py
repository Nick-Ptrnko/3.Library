"""
Створи клас Robot, метод __init__ якого приймає тільки name та записує його у властивість self.name,
a властивість self.partner спочатку None.
Створи функцію pair_robots, яка приймає список з двох імен, створює для кожного екземпляр класу Robot та
додає до кожного властивість partner з посиланням на партнера (інший об'єкт). Функція повертає кортеж з роботами.


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
    robot1 = Robot(robots[0])
    robot2 = Robot(robots[1])
    robot1.partner = robot2
    robot2.partner = robot1
    return robot1, robot2

robots = [
  'Alex',
  'Tom'
]
new_robots = pair_robots(robots)

print(new_robots[0].name == 'Alex')# True
all([isinstance(robot, Robot) for robot in new_robots]) # True
print(new_robots[0].partner is new_robots[1]) # True
print(new_robots[1].partner is new_robots[0]) # True
print([isinstance(robot, Robot) for robot in new_robots])