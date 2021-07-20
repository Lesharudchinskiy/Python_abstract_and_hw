from car_module_import import Car
from electric_car_module_import import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2018)
print(my_tesla.get_descriptive_name())
my_tesla.battery_size.describe_battery()
my_tesla.battery_size.get_range()