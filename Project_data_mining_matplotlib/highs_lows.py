# Comma Separated Values - запись данных в текстовый файл как серия значений, разделенных запятой
import csv
from datetime import datetime
from matplotlib import pyplot as plt
# Работа с данными:
#       Получение заголовков header_row:
# filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)   # метод reader(объект) - создает объект чтения данных
    header_row = next(reader)  # ф-ия next() - возвращает след. строку файла (сохраняем заголовки)
    # Печать заголовков и их позиций:
    # row - строка
    for index, column_header in enumerate(header_row):  # ф-ия enumerate(список) - для получения индекса каждого
        # элемента и его значения
        print(index, column_header)
    # Извлечение и чтение данных (извлечем максимальную температуру и дату):
    highs, dates, lows = [], [], []
    for row in reader:
        # Проверяем на наличие ошибок в полученном файле
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    # Нанесем полученные данные на диаграмму:
    fig = plt.figure(figsize=(16, 12))  # Задаем размер окна диаграммы
    plt.plot(dates, highs, c='red', alpha=0.5)  # передаем списки (макс темп и дата) и задаем цвет точек
    plt.plot(dates, lows, c='blue', alpha=0.5)  # передаем списки (мин темп и дата) и задаем цвет точек
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)  # alpha - степень прозрачности вывода (от 0 д 1)
    # Форматирование диаграммы:
    plt.title('Daily high and low temperatures - 2014\nDeath Valley, CA', fontsize=20)    # Заголовок
    plt.xlabel('', fontsize=16)     # Называем ось Х и задаем величину шрифта
    fig.autofmt_xdate()  # Наносим даты на ось Х
    plt.ylabel('Temperature (F)', fontsize=16)   # Называем ось У и задаем величину шрифта
    plt.tick_params(axis='both', which='major', labelsize=16)  # Увеличиваем отметки на осях и шрифт
    plt.show()


