julka = {'nickname': 'julka', 'kind_of_pet': 'dog', 'owner': 'diana'}
kesha = {'nickname': 'kesha', 'kind_of_pet': 'parrot', 'owner': 'lexa'}
markiza = {'nickname': 'markiza','kind_of_pet': 'cat', 'owner': 'sanya'}
pets = [julka, kesha, markiza]
for pet in pets:
    print("Pet's name: " + pet['nickname'].title())
    print('\tKind of pet: ' + pet['kind_of_pet'].title())
    print("\tOwner's name: " + pet['owner'].title())