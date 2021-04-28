# def sum_list(a, b):
#     new_list = list(zip(a, b))
#     for element in new_list:
#         yield sum(element)
#
#
# a = [2, 4, 6]
# b = [8, 5, 14]
#
# for i in sum_list(a, b):
#     print(i)
# return [a + b for a, b in zip(list1, list2)]
#
# --------------
#
# score = 1
# while True:
#     choice = input("Podaj liczbę lub napisz 'koniec' żeby zakończyć")
#     if choice == 'koniec':
#         break
#     score *= int(choice) if int(choice) % 2 == 0 else 1
# print(f'Twój wynik to: {score}')
#
# ----------------
#
# def get_factorial(a) -> int:
#     score: int = 1
#     for n in range(1, a + 1):
#         score *= ((a + 1) - n)
#     return score
#
#
# print(get_factorial(6))
#
# -------------------
#
# def count_vowels(text):
#     return sum([1 if char in 'aeiouy' else 0 for char in text])
#
# print(count_vowels('ala'))
# print(count_vowels('programowanie'))

# text = input('dej wyraz: ')
# vowels = []
# for char in text:
#     if char in 'aeiouy':
#         vowels += char
#
# print(len(vowels))

-------------------------


