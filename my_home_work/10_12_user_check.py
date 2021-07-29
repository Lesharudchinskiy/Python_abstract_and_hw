import json


def get_stored_name():
    filename = "username.json"
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input('Type your name: ')
    filename = "username.json"
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username


def check_username():
    username = get_stored_name()
    if username:
        answer = input(username + " Is this name is yours? Type: y/n ")
        if answer == "y":
            return username
        elif answer == "n":
            return None
    else:
        return None


def greet_user():
    username = check_username()
    if username:
        print("Welcome back " + username)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")


greet_user()
