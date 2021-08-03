from random import choice


class RandomWalk():
    """Инициируем начальные координаты и кол-во точек"""
    def __init__(self, num_points=5000):
        self.x_value = [0]
        self.y_value = [0]
        self.num_points = num_points

    def get_step(self):
        """Исходя из случайного направления и длины получаем шаг"""
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step

    def fill_walk(self):
        """Наносим нужное кол-во точкек с их шагами"""
        while len(self.x_value) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()
            # Если шаги равны нулю, то пропускаем итерацию
            if x_step == 0 and y_step == 0:
                continue
            # Делаем шаг от последней координаты
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step
            # Добавляем полученное значение
            self.x_value.append(next_x)
            self.y_value.append(next_y)
