import datetime
from json import dump
from datetime import date

date = datetime.date.today()
date = date.strftime('%d%m%Y')

list = []

product = input(f'Podaj nazwę produktu do zapisania: ')

while product != 'koniec':
    list.append(product)
    product = input(f'Podaj następny produkt do zapisania: ')

with open(f'{date}.txt', 'w') as data:
    dump(list, data)