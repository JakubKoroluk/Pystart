# łączenie liczb,
#
list1 = [1, 2, 3, 4, 5, 6]
list2 = [2, 3, 4, 5, 6, 7,]

print(list(zip(list1, list2)))
#
# first_name = ['Adam', 'Karol', 'Lukasz']
# last_names = ['Nowak', 'Kowalski', 'Drozd']
#
# for first_name, last_names in zip(first_name, last_names):
#     print(f'Imię to {first_name} , a nazwisko to {last_names}')
#
#
# pesel = '93070703834'
# check = '13791379131'
#
# control = 0
# for pesel_digit, check_digit in zip(pesel, check):
#     control += int(pesel_digit) * int(check_digit)
# if str(control)[-1] == '0':
#     print('Pesel jest OK')
# else:
#     print('Pesel jest nieprawudłowy')


