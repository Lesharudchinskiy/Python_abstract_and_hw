from random import randint


class Die():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        for brosok in range(10):
            self.sides = randint(1, self.sides)
            print(self.sides, end=' ')
        print('\n')


cube = Die()
print(cube.sides)
cube.roll_die()

cube = Die(10)
print(cube.sides)
cube.roll_die()

cube = Die(20)
print(cube.sides)
cube.roll_die()
