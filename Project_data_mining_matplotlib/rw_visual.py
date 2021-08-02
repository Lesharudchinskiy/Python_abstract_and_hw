import matplotlib.pyplot as plt

from random_walk import RandomWalk
while True:
    """Визуализируем случаные точки"""
    rw = RandomWalk(50000)
    # Необходимо вызвать метод класса
    rw.fill_walk()
    # Назначение размера области просмотра
    plt.figure(figsize=(16, 8))
    # Чтобы показать последовательность нанесения точек
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues, s=1)
    # Необходимо ставить перед plt.show(), чтобы точки выделились поверх остальных
    plt.scatter(rw.x_value[0], rw.y_value[0], c='green', s=100)  # Выделяем первую точку
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', s=100)  # Выделяем последнюю точку
    # Удаление осей (станут невидимыми):
    # plt.axes().get_xaxis().set_visible(False)
    # plt.axes().get_yaxis().set_visible(False)
    plt.show()

    keep_running = input("Type 'n' to exit or push any button: ")
    if keep_running == 'n':
        break
print('The end')
