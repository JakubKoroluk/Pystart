from json import dump


class Apple:
    def __init__(self, colour, taste, sort):
        self.colour = colour
        self.taste = taste
        self.sort = sort


class Basket:
    def __init__(self):
        self.apples = []

    def add(self, apple: Apple):
        self.apples.append(apple)


class Report:
    def __init__(self, basket):
        self.basket = basket

    def get_for_color(self):
        report = {}
        for apple in self.basket.apples:
            if apple.colour not in report:
                report[apple.colour] = 0

            report[apple.colour] += 1
        return report


def test_apple_collection():
    # given
    apple1 = Apple('red', 'sweet', 'ripe')
    apple2 = Apple('yellow', 'sweet', 'unripe')
    apple3 = Apple('orange', 'sweet', 'unripe')
    basket = Basket()

    # when

    basket.add(apple1)
    basket.add(apple2)
    basket.add(apple3)

    report = Report(basket)
    colors = report.get_for_color()

    # then
    assert colors == {
        'red': 1,
        'yellow': 1,
        'orange': 1
    }
