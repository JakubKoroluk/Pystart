# tempc = int(input('Podaj temperatruę w Celcjuszach'))
#
# tempf = tempc * 9 / 5
#
# print(f'Temperatura {tempc}C wynosi {tempf}F')
# from math import fabs

# Ax = int(input("Podaj wartość Ax"))
# Ay = int(input('Podaj wartość Ay'))
#
# Bx = int(input("Podaj wartość Bx"))
# By = int(input('Podaj wartość By'))
#
# Cx = int(input("Podaj wartość Cx"))
# Cy = int(input('Podaj wartość Cy'))
#
# AB = float((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 1 / 2
# BC = float((Cx - Bx) ** 2 + (Cy - By) ** 2) ** 1 / 2
# CA = float((Ax - Cx) ** 2 + (Ay - Cy) ** 2) ** 1 / 2
#
# print(f'AB={AB}, BC={BC}, CA={CA}')
#
# Ob = AB + BC + CA
# print(f'Obwód równa się {Ob}')
#
# Pabc = 1 / 2 * fabs((Bx - Ax) * (Cy - Ay) - (By - Ay) * (Cx - Ax))
#
# # print(f'Pole Trójkąta równa się {Pabc}')
#
# value = int(input('podaj liczbę'))
#
# if value % 5 == 0 and value % 11 == 0:
#     print(f'podzielna przez 5 i 11')
# elif value % 11 == 0:
#     print(f'podzielna przez 11')
# elif value % 5 == 0:
#     print(f'podzielna przez 5')
# else:
#     print(f'dupa')
import sys


class Bmi:
    SYSTEMS = ['METRYCZNY', 'IMPERIALNY']
    BMI = [((0, 16), 'wygłodzenie'), ((16.01, 16.99), 'wychudzenie'),
           ((17, 18.49), 'niedowaga'), ((18.5, 24.99), 'pożądana masa ciała'),
           ((25, 29.99), 'nadwaga'), ((30, 34.99), 'otyłość I stopnia'),
           ((35, 39.99), 'otyłość II stopnia (duża)'), ((40, 999), 'otyłość III stopnia (chorobliwa)')]

    def __init__(self):
        self.system = None
        self.weight = None
        self.height = None
        self.bmi = None
        self.gen_bmi()

    def print_menu(self):
        print('****** MENU ******')
        print(f"1. Wybierz system miar ({' / '.join(self.SYSTEMS)})")
        print('2. Podaj wagę(kg/funt)')
        print('3. Podaj wzrost(cm/cal)')
        print('4. Pokaż wprowadzone dane')
        print('5. Pokaż moje BMI')
        print('6. Exit')

    def exit(self):
        sys.exit()

    def get_system(self):
        while True:
            system = input("Podaj system miar: ")
            if system not in self.SYSTEMS:
                print(f"Dostępne opcje: {','.join(self.SYSTEMS)}")
                continue
            self.system = system
            break

    def calculate_bmi(self):
        if self.system is None or self.weight is None or self.height is None:
            print('niekompletne dane')
            return False
        else:
            if self.system == self.SYSTEMS[0]:
                result = round((self.weight / (self.height ** 2)) * 10000, 2)
            else:
                result = round((self.weight / (self.height ** 2)) * 703, 2)

            self.bmi = 'Coś poszło nie tak :('
            for q in self.BMI:
                if result >= q[0][0] and result <= q[0][1]:
                    self.bmi = f"{result} - {q[1]}"
                    break
            return True

    def get_weight(self):
        while True:
            try:
                weight = int(input("Podaj swoją wagę: "))
                self.weight = weight
                break
            except ValueError:
                print('Błędna waga!')
                continue

    def get_height(self):
        while True:
            try:
                height = int(input("Podaj swój wzrost: "))
                self.height = height
                break
            except ValueError:
                print('Błędny wzrost!')
                continue

    def show_data(self):
        print(f"System miar: {self.system}, Waga: {self.weight}, Wzrost: {self.height}")

    def gen_bmi(self):
        self.print_menu()
        while True:
            try:
                value = int(input("wybierz opcję: "))
                if value not in (1, 2, 3, 4, 5, 6):
                    print('nieznana opcja!!!!')
                    continue
                if value == 1:
                    if self.system is None:
                        self.get_system()
                    else:
                        print(f"System już podany ({self.system})!")
                    continue
                elif value == 2:
                    if self.weight is None:
                        self.get_weight()
                    else:
                        print(f"Waga już podana ({self.weight} kg/funt)!")
                    continue
                elif value == 3:
                    if self.height is None:
                        self.get_height()
                    else:
                        print(f"Wzrost już podany ({self.height} cm/cal)!")
                    continue
                elif value == 4:
                    self.show_data()
                    continue
                elif value == 5:
                    tmp = self.calculate_bmi()
                    if not tmp:
                        continue
                    else:
                        print('*' * 50)
                        print(f"Twoje BMI: {self.bmi}")
                        print('*' * 50)
                        break
                elif value == 6:
                    self.exit()
                break
            except ValueError:
                print('Błędna opcja!')
                continue


a = Bmi()