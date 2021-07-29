import json

filename = "favorite_number.json"
number = input("Type your favorite number: ")
with open(filename, 'w') as file_object:
    json.dump(number, file_object)
