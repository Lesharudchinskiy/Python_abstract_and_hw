file_name = 'learning_python.txt'

with open(file_name) as file_object:
    lines = file_object.read()

for _ in range(3):
    print('-' + lines)
    print()

with open(file_name) as file_object:
    lines2 = file_object.readlines()

for _ in range(3):
    for line2 in lines2:
        print('-' + line2.rstrip())
    print()