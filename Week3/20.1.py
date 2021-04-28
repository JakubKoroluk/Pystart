#
#
# def calculate_common_divisor(a, b, offset):
#     divisors_a = set()
#     divisors_b = set()
#     for i in range(2, a + 1):
#         if a % i == 0:
#             divisors_a.add(i)
#     for i in range(2, b + 1):
#         if b % i == 0:
#             divisors_b.add(i)
#     return divisors_a & divisors_b
#
#
# print(calculate_common_divisor(3, 6))
# print(calculate_common_divisor(3, 6, 4))
# print(calculate_common_divisor(16, 8))

def find_divisors(a):
    divisors = set()
    for divisor in range(2, a + 1):
        if a % divisor == 0:
            divisors.add(divisor)
    return divisors
    # return {divisors for divisor in range(2, a+1) if a % divisor == 0}


def calculate_common_divisor(a, b, offset=2):
    common_divisor = find_divisors(a) & find_divisors(b)
    common_divisor = [divisor for divisor in common_divisor if divisor >= offset]

    return sorted(common_divisor) if len(common_divisor) > 0 else None


print(calculate_common_divisor(3, 6))
print(calculate_common_divisor(3, 6, 4))
print(calculate_common_divisor(16, 8))
