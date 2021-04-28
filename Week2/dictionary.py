products = {
    'granaty': 3.5,
    'czarny proch': 10,
    'mp40': 100,
    'ak47': 400
}

# for product in products:
#     print(product)
#     print(products[product])

for name, price in products.items():
    print(f'nazwa: {name} \t\t cena: {price}')

product = input('Co podać?')
if product not in products:
    print('Nie mamy na stanie')
    quit()
# print(products[product])

price = products[product]
quantity = int(input('Należy podać ilość: '))
print(f'Do zapłaty {quantity * price} PLN')
