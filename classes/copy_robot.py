'''
Напиши функцію copy_robot, яка приймає robot екземпляр класу Robot, вона повинна повертати копію robot, але зі збільшеним serial_no на одиницю.
Приклад:
robot_copy is robot == False
robot_copy.model == 'g135'
robot.serial_no == 1664
robot_copy.serial_no == 1665
'''

class Robot:
    def __init__(self, model: str, constructor: str, serial_no: int) -> None:
        self.model = model
        self.constructor = constructor
        self.serial_no = serial_no

def copy_robot(robot: Robot) -> Robot:
    new_serial_no = robot.serial_no + 1
    new_robot = Robot(robot.model, robot.constructor, new_serial_no)
    return new_robot

robot = Robot('g135', 'Alex', 1664)
robot_copy = copy_robot(robot)

print(robot_copy.serial_no)
print(robot.serial_no)

print(robot_copy.model)
print(robot_copy.constructor)

print(robot_copy is robot)
