# for n in range(1, 11):
#     print(n)
#
# n = 1
# while n <= 10:
#     print(n)
#     n +=1
# PRIMES
# from math import floor
#
# primes = []
#
# n = 1
# while len(primes) < 10:
#     is_prime = True
#     for div in range(2, floor(n ** 0.5) + 1):
#         if n % div == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(n)
#     n += 1
# print(primes)
#
# AUTOBUS

bus_capacity = 100
pass_in_bus = 0

while bus_capacity >= pass_in_bus:
    pass_in_bus += int(input('Ile osób weszło teraz do busa? '))

    should_start = input('Ruszamy? tak/nie')
    if should_start == 'tak':
        break

    if pass_in_bus > bus_capacity:
        print(f' Ostatnie {pass_in_bus - bus_capacity} musi wyjść bo nikt nie pojedzie')
print('Autobus rusza')