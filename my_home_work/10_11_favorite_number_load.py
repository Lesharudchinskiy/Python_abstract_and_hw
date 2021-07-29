import json

filename = "favorite_number.json"
with open(filename) as file_object:
    f_num = json.load(file_object)
    print("I know your favorite number! This is " + f_num + "!")
