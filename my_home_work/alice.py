filename = 'alice in wonderland.txt'

try:
    with open(filename) as file_object:    # open порождает ошибку
        content = file_object.read()
except FileNotFoundError:
    print("Sorry, this file: " + filename + " doesn't exist")
else:
    # Подсчет приблизительного кол-ва слов в файле
    words = content.split()
    print("The file " + filename.title() + " has about " + str(len(words)) + " words")
