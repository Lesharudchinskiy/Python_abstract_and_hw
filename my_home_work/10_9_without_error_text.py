def animal_name(animal_type):
    try:
        with open(animal_type) as file_object:
            content = file_object.read()
            names = content.split()
    except FileNotFoundError:
        pass
    else:
        print("This file '" + animal_type + "' has following names of animals: ")
        for name in names:
            print(" - " + name.title())
        print("\n")


animal_type = "cats.txt"
animal_name(animal_type)

animal_type = "frogs.txt"
animal_name(animal_type)

animal_type = "dogs.txt"
animal_name(animal_type)