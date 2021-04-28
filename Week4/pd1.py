#
#
#
# def group_them(**kwargs):
#     result = (kwargs)
#     result = '\n'.join(' is '.join((key, val)) for (key, val) in result.items())
#
#     return result
#
# print(group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green'))
#
# ----------------------
#
# def fibonnaci_sum(num: int) -> int:
#     if number <= 0:
#         return 0
#     if num == 1 or num == 2:
#         return 1
#     return fibonnaci_sum(num - 2) + fibonnaci_sum(num - 1)
#
#
# number = 3
# fib_list = []
# for i in range(1, number + 1):
#     fib_list.append(fibonnaci_sum(i))
# print(fib_list, '=', sum(fib_list))
#
#

# def nwd(a,b):
#     rest = a % b
#     if rest == 0:
#         return b
#     return nwd(b,rest)
#
# print(nwd(282,78))


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def cut(start, end):
    def wrapper(function):
        def inner_wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            return result[start:end]
        return inner_wrapper()

    return wrapper


