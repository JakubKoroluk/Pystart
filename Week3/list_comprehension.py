# towrzymy liste []
# n + n to tworzenie podwójnej wartości
tup = [1, 9, 9, 1]
print(tup)
doubles = []
for n in tup:
    doubles.append(n ** 2)
print(doubles)



# new_list = []
# for n in range(1, 11):
#     if n % 2 == 0:
#         new_list.append('even')
#     else:
#         new_list.append('odd')
# print(new_list)
#
# new_list1 = ['even' if n % 2 == 0 else 'odd' for n in range(1, 11)]
# print(new_list1)

#
# names = ['Janek', 'Inga', 'Krzysiek', 'Basia']
# ladies = []
# for name in names:
#     if name[-1] == 'a':
#         ladies.append(name)
#
# print(ladies)
#
# ladies1 = [name for name in names if name[-1] == 'a']
# print(ladies1)

#
# persons = [
#     ('Janek', 'Wisniewski', 'Gdynia'),
#     ('Greg', 'Nowak', 'Warszawa'),
#     ('Alina', 'Norek', 'Gdańsk')
# ]
# persons_g = [person for person in persons if person[2][0] == 'G']
# person_upp = [(person[0], person[1], person[2].upper()) for person in persons_g]
# print(persons_g)
# print(person_upp)
# # lub
# person_2_in_1 = [(p[0], p[1], p[2].upper()) for p in persons if p[2][0] == 'G']
# print(person_2_in_1)
