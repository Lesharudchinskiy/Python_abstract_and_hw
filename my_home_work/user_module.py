class User():
    def __init__(self, first_name, last_name, age, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.full_name = self.first_name.title() + ' ' + self.last_name.title()

    def describe_user(self):
        info = 'Age: ' + str(self.age) + ', Location: ' + self.location.title()
        print('Full name: ' + self.full_name + '\n' + info)

    def greet_user(self):
        print('Hello, ' + self.full_name + '!')
