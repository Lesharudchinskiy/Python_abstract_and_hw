filename = 'guest_book.txt'

while True:
    print('If you want to exit: type "end"')
    name = input('Please, type your name here: ')
    welcome_text = 'You are WELCOME, ' + name.title()
    if name == 'end':
        break
    else:
        print(welcome_text)
        with open(filename, 'a') as f_object:
            f_object.write(welcome_text + '\n')
