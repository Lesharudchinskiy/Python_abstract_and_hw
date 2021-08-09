import csv
from datetime import datetime
from matplotlib import pyplot as plt
# Задаем файлы
filenames = ['sitka_weather_2014_1.csv', 'death_valley_2014_1.csv']
# Получаем заголовки
# Заполняем списки данных для Ситки:
highs_s, lows_s, dates, highs_dv, lows_dv = [], [], [], [], []
for filename in filenames:
    with open(filename) as f:
        reader = csv.reader(f)
        header_rows = next(reader)
        # Создаем пустые списки для данных
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                low = int(row[3])
                high = int(row[1])
            except ValueError:
                pass
            else:
                if filename == 'sitka_weather_2014_1.csv':
                    dates.append(current_date)
                    highs_s.append(high)
                    lows_s.append(low)
                elif filename == 'death_valley_2014_1.csv':
                    highs_dv.append(high)
                    lows_dv.append(low)
# Нанесем полученные данные на диаграмму:
fig = plt.figure(figsize=(16, 12))
plt.plot(dates, highs_s, c='red', alpha=0.5)
plt.plot(dates, lows_s, c='red', alpha=0.5)
plt.fill_between(dates, highs_s, lows_s, facecolor='red', alpha=0.1)
plt.plot(dates, highs_dv, c='blue', alpha=0.5)
plt.plot(dates, lows_dv, c='blue', alpha=0.5)
plt.fill_between(dates, highs_dv, lows_dv, facecolor='blue', alpha=0.1)
# Форматирование диаграммы:
plt.title('Daily high and low temperatures - 2014/01 \nDeath Valley, CA and Sitka', fontsize=20)    # Заголовок
plt.xlabel('', fontsize=16)     # Называем ось Х и задаем величину шрифта
fig.autofmt_xdate()  # Наносим даты на ось Х
plt.ylabel('Temperature (F)', fontsize=16)   # Называем ось У и задаем величину шрифта
plt.tick_params(axis='both', which='major', labelsize=16)  # Увеличиваем отметки на осях и шрифт
plt.show()

