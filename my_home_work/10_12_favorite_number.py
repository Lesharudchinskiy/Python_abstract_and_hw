import json

filename = "favorite_number.json"
try:
    with open(filename) as file_object:
        f_num = json.load(file_object)
except FileNotFoundError:
    f_num = input("Please, type your favorite number: ")
    with open(filename, 'w') as file_object:
        json.dump(f_num, file_object)
        print(f_num + "! I'll remember your favorite number in next time!")
else:
    print("Your favorite number is " + f_num + "!")
