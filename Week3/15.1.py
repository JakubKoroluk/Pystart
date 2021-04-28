# values = []
# while len(values) < 10:
#     value = input(f'Podaj jeszcze {10 - len(values)} liczb dodatnich: ')
#     if value > '0':
#         values.append(value)
# print(values)


values = []
value = int(input('Podaj liczbę: '))
values.append(value)
done = False
while not done:
    value2 = int(input('Podaj liczbę: '))

    if value2 < value:
        done = True
    else:
        value = value2
        values.append(value2)


print(values)
print(f'Średnia z tych liczb to {sum(values)/len(values)}')