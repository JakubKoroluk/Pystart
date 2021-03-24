# quantity = int(input('Ilość'))
# price = float(input('Cena'))
# amount = quantity * price
#
# print(f'Do zapłaty {amount}PLN')
#
#
# height = int(input('Podaj wzrost:'))
# weight = float(input('Podaj wagę:'))
#
# BMI = weight / (height**2)
#
# print(f'Twoje BMI wynosi :{BMI}')

netto = float(input('podaj cenę netto:'))
vat = float(input('podaj wysokość Vat:'))

brutto = netto * (1 + 0.01 * vat)

print(f'Cena Brutto wynosi {brutto}')
