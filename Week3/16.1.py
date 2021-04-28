podstawa = 2000

staz = int(input('Ile pełnych lat pracujesz: '))
sprzedaz = int(input('Ile sztuk towaru sprzedałeś: '))
godziny = int(input('Ile godzin miesięcznie pracujesz: '))

dodatek_stazowy = podstawa * 0, 1 if staz > 2 else podstawa * 0.02 * staz
dodatek_sprzedazowy = podstawa * 0.25 if sprzedaz >= 30 else 0
dodatek_godzinowy = podstawa * 0.08 if godziny > 160 and staz > 1 else podstawa * 0.02

zarobki = podstawa + dodatek_godzinowy + dodatek_sprzedazowy + dodatek_sprzedazowy
print(zarobki)
