def frequent_word_func(file_name, text_word):
    try:
        with open(file_name) as file_object:
            lines = file_object.read()
    except FileNotFoundError:
        pass
    else:
        number = lines.lower().count(text_word)
        print("The amount of word '" + text_word + "' is " + str(number))


word = 'row'
filename = "alice.txt"
frequent_word_func(filename, word)

word = 'row'
filename = "fly.txt"
frequent_word_func(filename, word)

word = 'row'
filename = "sedsf.txt"
frequent_word_func(filename, word)

