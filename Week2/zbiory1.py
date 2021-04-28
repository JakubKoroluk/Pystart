# divisible_3 = set(range(3, 1001, 3))
# divisible_5 = set(range(5, 1001, 5))
#
# print(
#     sorted(
#         list(divisible_5 & divisible_3)))

# name1 = "Bartek"
# name2 = 'Kacper'
#
# print(set(name1.lower()) ^ set(name2.lower()))
# print(set(name1.lower()) & set(name2.lower()))

emails = set()
for _ in range(10):
    emails.add(input('Podaj Adres email: '))

print(emails)

