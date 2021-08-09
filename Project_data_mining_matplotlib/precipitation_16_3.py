import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'sitka_weather_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    precs, dates = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            prec = float(row[-4])
        except ValueError:
            print('Information is missing!')
        else:
            precs.append(prec)
            dates.append(current_date)

fig = plt.figure(figsize=(10, 6))
plt.plot(dates, precs, c='red')
# Фоматирование диаграммы
plt.title('2014/01 Precipitation in Sitka', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Precipitation', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()