filename = 'guest.txt'

name = input()
with open(filename, 'w') as f_object:
    f_object.write(name.title())
