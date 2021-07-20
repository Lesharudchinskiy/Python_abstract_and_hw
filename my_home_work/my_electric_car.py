from car_class_import import ElectricCar

tesla_car = ElectricCar('tesla', 'model S', 2020)
print(tesla_car.get_descriptive_name())
tesla_car.battery_size.describe_battery()
tesla_car.battery_size.get_range()

