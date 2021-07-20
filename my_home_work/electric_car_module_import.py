from car_module_import import Car


class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range1 = 240
        elif self.battery_size == 85:
            range1 = 85
        message = "This car can go approximately " + str(range1)
        message += " miles on a full charge"
        print(message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    battery_size = Battery()
