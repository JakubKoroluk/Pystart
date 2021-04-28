# list1 = [16, 36, 25, 49]
#
#
# def map_and_filter(numbers: list) -> list:
#     return list(
#         filter(
#             lambda n: n % 2 == 0,
#             map(lambda n: n ** 0.5, list1)))
#
#
# def test_map_filter():
#     list1 = [16, 36, 25, 49]
#     assert map_and_filter(list1) == [4, 6]

people = ['zofia nowak', 'kryStyna kowalska', 'michał lewandowski']
def capitalize(word):
    return word[0].upper() + word[1:].lower()

def sort_names(persons:list) -> list:
    persons = map(lambda person: person.lower(), persons)
    persons = map(lambda person: person.split(' '), persons)
    persons = map(lambda person: capitalize(person[0]) + ' ' + capitalize(person[1]), persons)

    persons = sorted(persons, key=lambda person: person.split(' ')[1])
    return list(persons)

def test_sort_names():
    assert sort_names(people) == ['Krystyna Kowalska', 'Michał Lewandowski','Zofia Nowak']
