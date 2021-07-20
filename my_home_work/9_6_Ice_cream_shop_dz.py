class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is well known it's own " + self.cuisine_type + " cuisine!")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='ice creams'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['choco', 'nut', 'cola', 'fruit']

    def output_flavor(self):
        print(self.restaurant_name.title() + ' has flavors of ice cream: ')
#       print(*self.flavors)
        for flavor in self.flavors:
            print('-' + flavor.title())


mos_rest = IceCreamStand('moscow_ice')
mos_rest.output_flavor()
