from math import pi


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_field(self):
        field = pi * self.radius ** 2
        return field

    def calculate_circumference(self):
        area = 2 * pi * self.radius
        return area

if __name__ == '__main__':
    r = float(input('Podaj promień: '))
    circle1 = Circle(r)
    print(f'{circle1.calculate_field():.2f}')
    print(f'{circle1.calculate_circumference():.2f}')


#
# def test_circle_field():
#     # given
#     r = 10
#     c = Circle(r)
#
#     # when
#     field = c.calculate_field()
#
#     #
#     assert field == pi * r * r
#
#
# def test_circle_circumference():
#     # given
#     r = 10
#     c = Circle(r)
#
#     # when
#     circ = c.calculate_circumference()
#
#     assert circ == 2 * pi * r



