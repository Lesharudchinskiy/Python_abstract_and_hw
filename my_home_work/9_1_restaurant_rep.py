class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('The name of restaurant is ' + self.restaurant_name.title())
        print('The cuisine is a ' + self.cuisine_type)

    def open_restaurant(self):
        print('The restaurant ' + self.restaurant_name.title() + ' is open now !\n')


my_f_rest = Restaurant('mimino', 'caucasian')
print('The name of my favourite restaurant is ' + my_f_rest.restaurant_name.title() + '!')
print('My favourite cuisine is ' + my_f_rest.cuisine_type + '!\n')

my_f_rest.describe_restaurant()
my_f_rest.open_restaurant()

friends_f_rest = Restaurant('sushi', 'japanese')

friends_f_rest.describe_restaurant()
friends_f_rest.open_restaurant()

brothers_f_rest = Restaurant('papa_johns', 'italian')

brothers_f_rest.describe_restaurant()
brothers_f_rest.open_restaurant()
