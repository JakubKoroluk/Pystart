def count_letters(text, start='(', end=')'):
    should_count = False
    letters_counter = 0
    temp_counter = 0
    for char in text:
        if char == end:
            should_count = False
            letters_counter += temp_counter

        if should_count:
            temp_counter += 1

        if char == start:
            should_count = True
    return letters_counter



def test_count_letters():
    assert count_letters('Samuraj (programowania)') == 13

def test_count_letters_none():
    assert count_letters('Samuraj') == 0
    assert count_letters('Py(th)on', '<', '>') == 0

def test_multiple_brackets():
    assert count_letters('<Nauka> <programowania>', '<', '>') == 18

