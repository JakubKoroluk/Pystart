# def log(*args, **kwargs):
#     for arg in args:
#         print(type(arg), arg)
#     print(args)
#     print(kwargs)
#
# log(1, 2, 3, hello = 'Bartek')

def get_brutto(netto, vat):
    return netto + netto * vat


values = [
    (100, 0.23),
    (50, 0.05)
]

for value in values:
    print(get_brutto(*value))
