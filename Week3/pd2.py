# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 25, 16]
#
#
# def even_numbers(a):
#     return list([i for i in a if i % 2 == 0])
#
# print(even_numbers(a))
#
# ------------
#
# a = ['rabarbar', 'kon', 'banknot']
#
#
# def word_len(a):
#     return list([i for i in a if 4 < len(i) <= 8])
#
# print(word_len(a))
#
# -------------
#
# num1 = 8
# num2 = 16
#
#
# def max_divider(num1, num2):
#     dividers_a = (div for div in range(1, num1+1) if num1 % div == 0)
#     dividers_b = (div for div in range(1, num2+1) if num2 % div == 0)
#     # for i in range(1, num1+1):
#     #     if num1 % i == 0:
#     #         dividers_a.append(i)
#     # for i in range(1, num2+1):
#     #     if num2 % i == 0:
#     #         dividers_b.append(i)
#     # dividers = max(set(dividers_a) & set(dividers_b))
#     return max(set(dividers_a) & set(dividers_b))
#
#
# print(max_divider(num1, num2))
#
# ----------------

# def fibonnaci(a: int):
#     fibo = [0, 1]
#     n = 0
#     for i in range(2, a + 1):
#        n = fibo[i - 1] + fibo[i - 2]
#        fibo.append(n)
#     return fibo
#
# print(fibonnaci(2))

# def result_of_exam(a:int):
#     if a > 95: return 'celujący'
#     elif a > 90: return 'bardzo dobry'
#     elif a > 80: return 'dobry'
#     elif a > 55: return 'dostateczny'
#     elif a > 45: return 'dopuszczający'
#     else: return 'niedostateczny'
#
# print(result_of_exam(70))
#
#
#
#
#
# ____________


A = (2, 1)
B = (6, 8)


def len_of_AB(A: tuple, B: tuple):
    len_AB = ((B[0] - A[0]) ** 2 + (B[1] - A[1]) ** 2) ** 0.5
    return len_AB


print(len_of_AB(A, B))
