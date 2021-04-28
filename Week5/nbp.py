from  urllib.request import urlopen
from json import loads


with urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))
    rates = data[0]['rates']

    exchange = input('Jaką wartość chcesz wymienić na złotówki? ')
    value, code = exchange.split(' ')
    value = float(value)

    rate = list(filter(lambda x: x['code'] == code, rates))
    print(f'Otrzymujesz {value * rate[0]["mid"]} PLN')

