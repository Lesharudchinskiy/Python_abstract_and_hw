import car_class_import

my_beetle = car_class_import.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_class_import.ElectricCar('tesla', 'model s', 2018)
print(my_tesla.get_descriptive_name())
