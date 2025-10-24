class Robots:
    def __init__(self, model):
        self.model = model
        self.parts_made = 0
    def make_part(self):
        self.parts_made += 1

robot1 = Robots("Robot 1")
robot1.make_part()
robot1.make_part()
print(robot1.parts_made)
