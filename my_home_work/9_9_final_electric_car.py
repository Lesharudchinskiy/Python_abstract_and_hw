
class Car():

    def __init__(self, make, model, year):
        """Инициируем атрибуты описания авто"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает аккуратно отформатированное описание авто"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name

    def read_odometer(self):
        """Выводит пробег машины в милях"""
        print('This car has ' + str(self.odometer_reading) + ' miles on it')


class Battery():   # Класс как экземпляр
    """Простая модель аккумулятора электромобиля"""

    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):   # Добавим еще 1 метод потомку
        """Выводит приблизительный запас хода для аккумулятора"""
        if self.battery_size == 70:
            range_ = 240
        elif self.battery_size == 85:
            range_ = 270
        message = "This car can go approximately " + str(range_)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
            print('Now the battery size is 85kWh!')


class ElectricCar(Car):
    """Потомок класса Car"""
    def __init__(self, make, model, year):
        """Инициируем атрибуты"""
        super().__init__(make, model, year)
        self.battery_size = Battery()   # Автоматически создаваемый экземпляр Battery()
        # Приказывает Python создать новый экземпляр Battery() (со знач. по молчанию battery_size=70) и сохранить его в
# battery_size


tesla_car = ElectricCar('tesla', 'model S', 2018)
tesla_car.battery_size.get_range()
tesla_car.battery_size.upgrade_battery()
tesla_car.battery_size.get_range()
