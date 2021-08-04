# Гистограмма - столбцовая диаграмма
import pygal
from die import Die
# Создаем экземпляк кубика (по умолчанию 6 грайней)
die = Die()
# Создаем пустой список для записи всех бросков
throws = []
# Получаем случайные броски в нужно кол-ве
for throw in range(1000):
    result = die.roll()
    throws.append(result)
# print(throws)

# Создаем список кол-ва выброшенных одинаковых чисел
frequencies = []
# Из кол-ва сторон создаем цикл (Анализ результатов)
for side in range(1, 7):
    # Считаем кол-во
    count_num = throws.count(side)
    # Добавляем в список
    frequencies.append(count_num)
# print(frequencies)

# Визуализация результатов
hist = pygal.Bar()  # Создаем экземпляр

hist.title = "Results of rolling one D6 1000 times"   # Атрибут - title (заголовок гистограммы)
hist.x_labels = ['1', '2', '3', '4', '5', '6']  # Метки на оси х
hist._x_title = "Result"  # Заголовок оси Х
hist.y_title = "Frequency of Result"  # Заголовок оси У
# Добавляем на гистограмму серию значений :
hist.add('D6', frequencies)
# Записываем в файл гистограмму
hist.render_to_file('die_visual.svg')
