from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print(*[randint(1, self.sides) for _ in range(10)])  # генертруем списк и раскрываем его


cube = Die()
print(cube.sides)
cube.roll_die()

cube = Die(10)
print(cube.sides)
cube.roll_die()

cube = Die(20)
print(cube.sides)
cube.roll_die()
