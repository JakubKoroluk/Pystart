# word1 = input('Wpisz pierwszy wyraz: ')
# word2 = input('Wpisz drugi wyraz: ')
#
# set1 = set(word1)
# set2 = set(word2)
#
# counter1 = {}
# counter2 = {}
#
# if set1 ^ set2 is not None:
# # palindrom czyli od tyłu taki sam wyraz
#     if word1 == word2[::-1]:
#         print('Podane słowa są palindromem')
#         quit()
# # Sprawdzenie czy są anagramem
# set1 = list(word1)
# set2 = list(word2)
#
# for i in sorted(set1):
#     if i not in counter1:
#         counter1[i] = 1
#     else:
#         counter1[i] += 1
# for n in sorted(set2):
#     if n not in counter2:
#         counter2[n] = 1
#     else:
#         counter2[n] += 1
# print(counter1)
# print(counter2)
#
# if counter1 == counter2:
#     print('Podane słowa są anagramem')
# else:
#     print('Podane słowa są niczym')
import math

value_min = int(input('Wpisz najmniejszą wartość: '))
value_max = int(input('Wpisz największą wartość: '))

values = list(range(value_min, value_max + 1))
print(values)

for n in values:
    p = 2
    while p < math.sqrt(value_max):
        for i in range(p, value_max + 1):
            if p * i in values:
                values.remove(p * i)
        p += 1
print(values)
#
# word1 = input('Wpisz pierwszy wyraz')
# word2 = input('Wpisz drugi wyraz')
#
# word1 = set(word1)
# word2 = set(word2)
#
# print(word1)
# print(word2)
#
# wspolne = word1 & word2
#
# print(wspolne)

sentence = input('Wypisz słowa po przecinku: ').split(',')

sentence = list(sentence)

for i in sentence:
    print(i,)
