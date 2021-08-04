from random import randint


class Die():
    """Класс , представляющий один кубик"""
    def __init__(self, num_sides=6):
        # Задаем поумолчанию 6-ти сторонний кубик
        self.num_sides = num_sides

    def roll(self):
        # Моделируем выброшенный результат от 1 до кол-ва сорон
        return randint(1, self.num_sides)
