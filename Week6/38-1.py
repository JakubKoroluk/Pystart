class Product:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def __str__(self):
        return f'{self._name}, koszt: {self._price}'

    def get_price(self) -> float:
        return self._price


class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._quantity = quantity
        self._product = product

    def get_quantity(self) -> float:
        return self._quantity

    def get_product(self) -> Product:
        return self._product

    def get_subtotal(self) -> float:
        return self._quantity * self._product.get_price()

    def increase_quantity(self, quantity):
        self._quantity += quantity

    def dicrease_quantity(self, quantity):
        self._quantity -= quantity


class List:
    def __init__(self):
        self._items = []

    def add_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.increase_quantity(quantity)
                return
        self._items.append(
            ListItem(product, quantity)
        )

    def remove_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.decrease_quantity(quantity)
                return

    def list_items(self):
        return self._items

    def calculate_total_cost(self) -> float:
        total = 0
        for item in self._items:
            total += item.get_subtotal()
        return total


def test_add_item_to_list_once():
    # given
    product = Product('Chleb', 4.30)
    to_buy = List()
    # when
    to_buy.add_item(product, 3)

    # then
    assert to_buy.calculate_total_cost() == 4.3 * 3
    assert len(to_buy.list_items()) == 1


def test_add_the_same_item_to_list_twice():
    # given
    product = Product('Chleb', 4.30)
    to_buy = List()
    # when
    to_buy.add_item(product, 3)
    to_buy.add_item(product, 3)
    # then
    assert to_buy.calculate_total_cost() == 4.3 * 6
    assert len(to_buy.list_items()) == 1


def test_add_two_different_product():
    # given
    product1 = Product('Chleb', 4.30)
    product2 = Product('Masło', 5.30)
    to_buy = List()
    # when
    to_buy.add_item(product1, 2)
    to_buy.add_item(product2, 1)

    # then
    assert to_buy.calculate_total_cost() == 4.3 * 2 + 5.30 * 1
    assert len(to_buy.list_items()) == 2
