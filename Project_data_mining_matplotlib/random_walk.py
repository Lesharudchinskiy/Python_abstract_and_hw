from random import choice


class RandomWalk():
    """Инициируем начальные координаты и кол-во точек"""
    def __init__(self, num_points=5000):
        self.x_value = [0]
        self.y_value = [0]
        self.num_points = num_points

    def fill_walk(self):
        while len(self.x_value) < self.num_points:
            # Случаный сдвиг по оси х
            x_direction = choice([-1, 1])
            x_distance = choice([1, 2, 3, 4])
            x_step = x_direction * x_distance

            # Случаный сдвиг по оси y
            y_direction = choice([-1, 1])
            y_distance = choice([1, 2, 3, 4])
            y_step = y_direction * y_distance
            # Если шаги равны нулю, то пропускаем итерацию
            if x_step == 0 and y_step == 0:
                continue
            # Делаем шаг от последней координаты
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            # Добавляем полученное значение
            self.x_value.append(next_x)
            self.y_value.append(next_y)
