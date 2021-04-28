pesel = input('Wprowadź PESEL: ')
check_list = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3, 1)

sum_of_pesel = 0
pesel = list(pesel)

if len(pesel) != 11:
    print('Wprowadź właściwą ilość cyfr.')
else:
    for i in range(11):
        sum_of_pesel += int(pesel[i]) * check_list[i]
    if str(sum_of_pesel)[-1] == '0':
        print('pesel jest prawidłowy')
    else:
        print('Pesel jest nie prawidłowy')

