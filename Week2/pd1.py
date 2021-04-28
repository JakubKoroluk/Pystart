# value = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie'
# value = value.lower()
# list_of_words = value.split()
# print(list_of_words)
#
#
# # print(value.count('pies'))
#
# number_of_pies = 0
#
# for word in list_of_words:
#     if word == 'pies':
#         number_of_pies += 1
# print(f'Pies występuje {number_of_pies} razy')

sentence = '12 kilogamów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'
numbers = []
sentence = sentence.split()

for word in sentence:
    if word.isdigit():
        numbers.append(int(word))

sum_of_numbers = sum(numbers)

print(sum_of_numbers)
