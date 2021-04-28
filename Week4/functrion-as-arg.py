# def total_salary(base, extra):
#     return base + extra(base)
#
#
# def calculate_ten_percent(amount):
#     return 0.1 * amount
#
#
# print(total_salary(1000, calculate_ten_percent))
#
# power = lambda x: x ** 2
# sum_numbers = lambda a, b: a * b

numbers = [1, 5, 10, 9, 7]

doubles = [n + n for n in numbers]
doubles = map(lambda n: n + n, numbers)

filtered = [n for n in numbers if n % 2 == 0]
filtered = filter(lambda n: n % 2 == 0, numbers)

