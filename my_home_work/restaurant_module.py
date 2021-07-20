class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name.title() + " is well known it's own " + self.cuisine_type + " cuisine!")

    def open_restaurant(self):
        print(self.restaurant_name.title() + " is open now!")
