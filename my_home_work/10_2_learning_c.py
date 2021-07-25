file_name = 'learning_python.txt'

with open(file_name) as f_object:
    lines = f_object.readlines()

for line in lines:
    if 'Python' in line:
        print(line.replace('Python', 'C').rstrip())
