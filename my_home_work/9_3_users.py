class User():
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print('The info about user:')
        print(self.first_name.title(), self.last_name.title())
        print('Age: ' + str(self.age) + ', Country: ' + self.country.title() + '\n')

    def greet_user(self):
        print('Hello, ' + self.first_name.title(), self.last_name.title() + '!')


nik_user = User('nikolay', 'tushkanov', 55, 'russia')
daniel_user = User('daniel', 'merin', 38, 'usa')
alex_user = User('alexander', 'fominskiy', 28, 'israel')

nik_user.greet_user()
nik_user.describe_user()
daniel_user.greet_user()
daniel_user.describe_user()
alex_user.greet_user()
alex_user.describe_user()
