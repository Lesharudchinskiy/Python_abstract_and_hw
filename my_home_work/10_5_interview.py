filename = 'interview.txt'

while True:
    print('If you want to exit, type: "end"')
    question = 'Why do you like to programming, type the reason here: '
    reason = input(question)
    if reason == 'end':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write('The answer was: - ' + reason + '\n')
