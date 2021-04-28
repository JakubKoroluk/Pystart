# def to_round(function):
#     def wrapper(*args, **kwargs):
#         result = function(*args, **kwargs)
#         return round(result, 2)
#
#     return wrapper
#
#
# def test_to_round():
#     @to_round
#     def return_round():
#         return 2.12145
#
#     result = return_round()
#
#     assert result == 2.12
#
# @to_round
# def return_round():
#     return 14.12555
#
# print(return_round())

