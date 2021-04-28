a = 'lalka'

b = 'k'


def convert(string):
    list_of_words = []
    list_of_words[:0] = string
    return list_of_words


def check_word(a:str, b:str):
    list_a = convert(a)
    if b in list_a:
        return b
    else:
        return None




print(check_word(a, b))

print(convert(a))

print()
