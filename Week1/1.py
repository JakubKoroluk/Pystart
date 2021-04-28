height = int(input('Podaj wzrost:'))
weight = float(input('Podaj wagę:'))

BMI = weight/((0.01 * height)**2)

print(f'Twoje BMI wynosi :{BMI:.2f}')

# a = int(input('Podaj długość boku a'))
# b = int(input('Podaj długość boku b'))
# h = int(input('Podaj długość boku h'))
#
# tr_field = (a + b)/2 * h
#
# input(f'Pole trapezu wynosi {tr_field}')
