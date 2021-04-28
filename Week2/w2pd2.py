word = input('Wpisz wyraz: ')

word = list(word)
counter = {}
print(word)
for i in sorted(word):
    if i not in counter:
        counter[i] = 1
    else:
        counter[i] += 1

print(counter)
