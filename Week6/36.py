class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100

    def __add__(self, other):
        total = self.value + other.value
        return LengthUnit(total)

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        return self.value == other.value


a = LengthUnit(10)
b = LengthUnit(20)

c = a + b
print(a.value + b.value)

d = b - a
print(d)

print(a == b)


def add_length_units():
    # given
    a = LengthUnit(10)
    b = LengthUnit(20)

    # when
    c = a + b

    # then
    assert c.value == 30

