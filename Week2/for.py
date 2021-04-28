# for i in range(1, 21):
#     if i % 3 == 0:
#         print(i)
#
# names = ['Ada', 'Bill', 'Steve', 'Mark', 'Martha']
# for name in names:
#     if len(name) > 4:
#         print(name)
#

# numbers = list(range(1, 100))
#
# numbers_div_by_4 = 0
# numbers_div_by_5 = 0
#
# for number in numbers:
#     if number % 4 == 0:
#         numbers_div_by_4 += 1
#
#     if number % 5 == 0:
#         numbers_div_by_5 += 1
#
# print(f'Liczby podzielne przez 4  = {numbers_div_by_4}')
# print(f'Liczb podzielnych przez 5  = {numbers_div_by_5}')
#
# _____
# names = ['Ada', 'Bill', 'Steve', 'Mark', 'Martha', 'John']
#
# shortest_name = None
# longest_name = None
#
# print(names)
# for name in names:
#     if shortest_name is None or len(name) < len(shortest_name):
#         shortest_name = name
#     if longest_name is None or len(name) > len(longest_name):
#         longest_name = name
#
# print(f'Najkrótsze imię to {shortest_name}')
# print(f'Najdłuższę imię to {longest_name}')

# value = int(input('Podaj liczbę'))
#
# is_prime = True
# value_sqrt = int(value ** 0.5)
# # lub sqrt(value) a wcześniej from math import sqrt
#
# for x in range(2, value_sqrt + 1):
#     if value % x == 0:
#         is_prime = False
#         print(f'{x} jest dzielnikiem')
#         break
#
# if is_prime:
#     print('Liczba jest pierwsza')
# else:
#     print('Liczba nie jest pierwsza')

# value = int(input('Podaj Liczbę: '))
#
# for row in range(1, value + 1):
#     for col in range(1, value + 1):
#         print(col, end=' ')
#     print('')
#     value -= 1

# Enumerate


books = ['w pustyni', 'w puszczy', 'cos jeszcze']
for book_id, book in enumerate(books, start=1):
    print(book_id, book)
