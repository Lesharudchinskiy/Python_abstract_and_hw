def city_country(city, country):
    pair = city.title() + ' ' + country.title()
    return pair

while True:
    print('If you want to quit, type "q"')
    c = input('Enter city: ')
    if c == 'q':
        break

    countr = input('Enter country: ')
    if countr == 'q':
        break

    print(city_country(c, countr))
