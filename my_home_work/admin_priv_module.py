from user_module import User


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
