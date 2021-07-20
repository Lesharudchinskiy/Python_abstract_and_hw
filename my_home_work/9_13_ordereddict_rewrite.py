from collections import OrderedDict
glossariy = OrderedDict()

glossariy['list'] = 'список'
glossariy['tuple'] = 'кортеж'
glossariy['dictionary'] = 'словарь'
glossariy['slice'] = 'срез'
glossariy['integer'] = 'целые числа'

for word, meaning in glossariy.items():
    print(word + " : " + meaning)
