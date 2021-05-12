class Car:
    def __init__(self, name: str, price: int, max_speed: int):
        self.name = name
        self.price = price
        self.max_speed = max_speed

    def get_info(self):
        return f'{self.name}, cena: {self.price}, Vmax: {self.max_speed}'


class Collection:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def get_items(self, key, reverse = False):
        return sorted(self.items, key=key, reverse=reverse)



if __name__ == '__main__':

    collection = Collection()

    for _ in range(2):
        name = input('Nazwa: ')
        price = int(input('Cena: '))
        max_speed = int(input('Vmax: '))
        collection.add_item(Car(name, price, max_speed))

    for car in collection.get_items(key=lambda c: c.price, reverse=True):
        print(car.get_info())


def test_class_car():
    car = Car(name='Polonez', price=1500, max_speed=160)

    assert isinstance(car, Car)
    assert car.name == 'Polonez'
    assert car.price == 1500
