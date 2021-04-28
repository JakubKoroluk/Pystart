tekst = 'Szedł (koń) do (baru) bo (piwka) mu się (chciało)'


def count_letters(text: str, start='(', end=')'):
    text = text.split()
    len_of_words = []
    for i in text:
        if '(' in i:
            len_of_words.append(len(i) - 2)
    return len_of_words


print(count_letters(tekst))
