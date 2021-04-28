from urllib.request import urlopen
from json import loads

with urlopen("https://danepubliczne.imgw.pl/api/data/synop") as site:
    data = loads(site.read())
    print(data)

    city = input('Podaj miasto żeby poznać aktualną pogodę: ')
    # chosen_city = list(filter(lambda x: x['stacja'] == city, data))
    chosen_city = list([i for i in data if i['stacja'] == city])
    print(f'Stacja: {chosen_city[0]["stacja"]}\nOstatni pomiar: {chosen_city[0]["data_pomiaru"]}\nTemperatura: {chosen_city[0]["temperatura"]} Stopni\n')
