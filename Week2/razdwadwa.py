sentence = 'raz dwa dwa trzy trzy trzy cztery'.split()

dictionary = {}
for i in sentence:
    if i not in dictionary:
        dictionary[i] = 1
    else:
        dictionary[i] += 1
print(dictionary)
