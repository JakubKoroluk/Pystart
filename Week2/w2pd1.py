# word = list(input('Wpisz wyraz: '))
# counter = {}
#
# print(word)
#
# for i in word:
#     if i not in counter:
#         counter[i] = 1
#     else:
#         counter[i] += 1
#
# print(counter)

# value = int(input('Podaj liczbę w systemie dziesiętnym: '))
# binn = ''
# for i in range(0, int(value)):
#     n = value
#     value = int(n)
#         while int(value) // 2 > 0:
#         if value % 2 == 0:
#             binn += '0'
#         else:
#             binn += '1'
#         value = value // 2
#     print(bin)
#
# print(ord('a'))
# print(ord('1'))
# print(ord('z'))
#
# word = input('Podaj treść do zaszyfrowania: ')
# new_word = ''
#
# for i in word:
#     if 49 < ord(i) <= 97:
#         change = ord(i) + 3
#         if change >= 97:
#             change -= 26
#         new_word += chr(change)
#     elif 98 <= ord(i) < 122:
#         change = ord(i) + 3
#         if change >= 122:
#             change -= 57
#         new_word += chr(change)
#     else:
#         new_word += i
# print(new_word)

if option == '1':
    result = ''
    for char in text:
        if ord(char) >= ord('x')
            result += chr(ord(char) - 23)
        else:
            result += chr(ord(char) + 3)
elif option == '2':
    result = ''
    for char in text:
        if ord(char) >= ord('d')
            result += chr(ord(char) - 3)
        else:
            result += chr(ord(char) + 23)
