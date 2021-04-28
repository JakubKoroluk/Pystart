# def bill_off_energy(hours: int, power_consumption: int, kwh=0.617):
#     cost = round(float((int(hours) * int(power_consumption)) * float(kwh * 1000)), 2)
#     return cost
#
#
# hour = int(input('Podaj liczbę godzin: '))
# power_cons = int(input('Podaj zapotrzebowanie energii w W: '))
#
# print(f' Zapłacisz {bill_off_energy(hour, power_cons)} PLN')

def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    odds = [odd in odd for odd in numbers if odd % 2 != 0]
    evens = [even in even for even in numbers if even % 2 == 0]

    total = 0 if not count_odd else len(odds)
    total += 0 if not count_even else len(evens)
