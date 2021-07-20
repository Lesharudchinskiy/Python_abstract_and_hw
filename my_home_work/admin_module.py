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


class Privileges():
    def __init__(self, privileges=['allow_add_message', 'allow_delete_users', 'allow_ban_users']):
        self.privileges = privileges

    def show_privileges(self):
        print('Admin has these privileges: ')
        for privilege in self.privileges:
            print('-' + privilege)


class Admin(User):
    def __init__(self,  first_name="Admin", last_name="", age="", location=""):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()