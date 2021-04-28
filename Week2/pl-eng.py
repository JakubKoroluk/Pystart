# dictionary = {
#     'kot': 'cat',
#     'pies': 'dog',
#     'dom': 'house',
#     'mysz': 'mouse'
# }
#
# print('1 - Przetłumacz z polskiego na angielski')
# print('2 - Przetłumacz z angielskiego na polski')
#
# question = int(input('Wybierz opcję z dostępnych powyżej: '))
#
#
# if question == 1:
#     for pl, eng in dictionary.items():
#         print(pl)
#     word_pl = input('Wybierz słowo do przetłumaczenia: ')
#     if word_pl in dictionary:
#         word_eng = dictionary[word_pl]
#         print(f' {word_pl} to po angielsku {word_eng}')
#     else:
#         print('Słowo nie występuje w słowniku.')
# elif question == 2:
#     for pl, eng in dictionary.items():
#         print(eng)
#     word_eng = input('Wybierz słowo do przetłumaczenia: ')
#     if word_eng in dictionary.values():
#         word_pl = dictionary[word_eng]
#         print(f'{word_eng} to po polsku {word_pl}')
#     else:
#         print('Słowo nie występuje w słowniku.')
# else:
#     print(f'No i nie podobasz mi się kolego')

animals = {
    'kot': 'cat',
    'pies': 'dog',
    'dom': 'house',
    'mysz': 'mouse'
}
pol_ang = input("Jeśli chcesz przetłumaczyć z polskiego na angielski naciśnij '1' jeśli odwrotnie '2' ")


if pol_ang == '1':
    word = input("Podaj nazwę zwierzaka ")
    if word in animals:
        print(animals[word])
        quit()
    print('Brak tłumaczenia')
elif pol_ang == '2':
    word = input("Podaj nazwę zwierzaka ")
    for pol, ang in animals.items():
        if ang == word:
            print(pol)
            quit()
    print('Brak tłumaczenia')
else:
    print('Wybierz jeszcze raz')
