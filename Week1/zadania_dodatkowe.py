# def make_readable(seconds):
#     hh = 0
#     mm = 0
#     ss = 0
#
#     while seconds >= 3600:  # mamy 7200, program widzi ponad 3600 więc dodaje jedną godzinę, odejmuje 3600.
#         hh += 1
#         seconds -= 3600
#
#     while seconds >= 60:  # kiedy program zobaczy poniżej 3600, zejdzie do tej instrukcji
#         mm += 1
#         seconds -= 60
#     ss = seconds
#
#     return "{:2}:{:02}:{:02}".format(hh, mm, ss)
#
#
# print(make_readable(23400))
# print(make_readable(43200))
# print(make_readable(81000))

# Zadanie 2
# Szef kazał napełniać pracownikowi butelki 330 ml cieczą, w taki sposób by 12% butelki
# pozostawało puste. Pracownik umówił się z szefem, że cały płyn który mu pozostanie i nie
# wystarczy do napełnienie butelek może zostawić sobie. Po starcie odbierz od użytkownika
# informację ile ml płynu dostarczyła fabryka, a wynikiem powinna być ilość cieczy, którą
# pracownik będzie mógł wziąć ze sobą :)

# bottle_volume = 330
#
# empty_part_bottle = 0.12
#
# liquid_to_split = int(input('Podaj ilość płynu do rozlania [ml]'))
#
# full_bottles = liquid_to_split / (bottle_volume * (1 - empty_part_bottle))
# liq_for_worker = liquid_to_split % (bottle_volume * (1 - empty_part_bottle))
#
# print(f'Napełnionych zostało {round(full_bottles)} butelek ')
# print(f'Pracownik może zabrać {round(liq_for_worker)}ml płynu')
#
# Zadanie 3
# Przygotuj dwie zmienne, zawierające kurs kupna oraz kurs sprzedaży USD. Na dzień
# dzisiejszy to kupno 3.8507, sprzedaż 3,9285. Twoim zadaniem będzie zapytać użytkownika o
# to co chce zrobić kupić/sprzedać, następnie zapytać go o ilość złotówek lub dolarów do
# # wymiany, a następnie poinformować jaką wartość po wymianie użytkownik otrzyma.
#
#
# PLN_USD = 3.8507
# USD_PLN = 3.9285
#
#
#
# while True:
#     print('1. Kup dolany')
#     print('2. Sprzedaj dolany')
#     option = int(input('Wybierz opcję z powyższych:'))
#     if int(option == 1):
#         pln = float(input('Wprowadź ilość PLN: '))
#         change1 = pln / PLN_USD
#         print(f'Kupiłeś {round(change1, 2)} USD za {pln}PLN')
#     elif int(option == 2):
#         usd = float(input('Wprowadź ilość USD: '))
#         change2 = usd * USD_PLN
#         print(f'Sprzedałeś {usd} USD za {round(change2, 2)} PLN')
#     else:
#         print('Spróbuj jeszcze raz')
#         print('1. Kup dolany')
#         print('2. Sprzedaj dolany')

# from prettytable import prettytable
#
# table = prettytable.PrettyTable()
# table.field_names = ['Plan dnia', 'Informacja od programu', 'Jaki to czas?']
#
# minutes1 = 23400 / 60  # sekundy na 60 dają nam ilość minut
# minutes2 = 43200 / 60
# minutes3 = 81000 / 60
#
# hours1, minutes1 = divmod(minutes1, 60)
# hours2, minutes2 = divmod(minutes2, 60)
# hours3, minutes3 = divmod(minutes3, 60)
#
# table.add_row(['Pobudka', 23400, ('%02d:%02d' % (hours1, minutes1))])
# table.add_row(['Czas na lunch', 43200, ('%02d:%02d' % (hours2, minutes2))])
# table.add_row(['Czas spać', 81000, ('%02d:%02d' % (hours3, minutes3))])
#
# print(table)

# Zadanie 4
# Odbierz od użytkownika dwa dowolne punkty na płaszczyźnie(x1, y1, x2, y2), które tworzą
# odcinek. Znajdź jego środek. i wypisz jakie jest pole oraz promień okręgu, którego ten
# odcinek jest średnicą. Poszło? To zastanów się jakie pole i obwód ma prostokąt którego ten
# odcinek jest przekątną :-)
#
# import math
#
# x1 = int(input('Podaj współrzędną x1: '))
# y1 = int(input('Podaj współrzędną y1: '))
# x2 = int(input('Podaj współrzędną x2: '))
# y2 = int(input('Podaj współrzędną y2: '))
#
# Sx = (x1 + x2) / 2
# Sy = (y1 + y2) / 2
#
# print(f'Środek odcinka S: ({Sx},{Sy})')
#
# AB = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 1 / 2
# r = AB / 2
#
# print(f'Promień wynosi {r}')
#
# circle_area = math.pi * r ** 2
#
# print(f'Pole koła o promieniu {r} wynosi {round(circle_area, 1)}')

# Zadanie 5
# Przygotuj program, który na podstawie wieku urodzenia danej osoby, odpowie ile ta osoba
# ma lat, czy jest pełnoletnia oraz czy rok w którym się urodziła był rokiem przestępnym.
# Zwróć uwagę, że taki rok nie zawsze przypada co cztery lata :) Rok bieżący możesz
# przechowywać w jednej zmiennej zadeklarowanej na początku programu.

#
# import datetime
#
# print(f'Podaj swoją datę urodzin: ')
# year_of_birth = int(input('Podaj rok: '))
# month_of_birth = int(input('Podaj miesiąc: '))
# day_of_birth = int(input('Podaj dzień: '))
#
# date_of_birth = datetime.date(year_of_birth, month_of_birth, day_of_birth)
# date = datetime.date(2021, 3, 12)
# print(date_of_birth)
# print(date)
#
# diffrent = date - date_of_birth
#
# age = round(diffrent.days / 365, 1)
#
# if age >= 18:
#     print(f'Masz {age} lat więc jesteś pełnoletni.')
# else:
#     print(f'Masz {age} lat więc jesteś niepełnoletni')

Zadanie 6
Zapytaj użytkownika o długość boku trójkąta równobocznego. Odpowiedz jakie jest pole
tego trójkąta oraz jaka będzie objętość stożka powstała przez obrót tego trójkąta wokół osi,
którą jest jego wysokość .