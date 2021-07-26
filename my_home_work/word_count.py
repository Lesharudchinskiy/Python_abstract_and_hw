def count_words(filename):
    """Подсчет приблизительного количества строк в файле"""
    try:
        with open(filename) as f_object:
            content = f_object.read()
    except FileNotFoundError:
        print('Sorry, the file: ' + filename + " does not exist")
    else:
        words = content.split()
        num_words = len(words)
        print("This file " + filename + "has about " + str(num_words) + " words.")


filenames = ['theft.txt', 'shaming.txt', 'fly.txt', 'alice.txt']
for filename in filenames:
    count_words(filename)
