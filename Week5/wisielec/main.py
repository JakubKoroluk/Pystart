import tkinter as tk
from random_word import RandomWords

# To keep bad answers from user
answers = []
counter = 0
word_to_find = ''
word = ''

r = RandomWords()
# Return a single random word
random_word = r.get_random_word()
random_word = random_word.lower()
print(random_word)



def convert(string):
    list_of_words = []
    list_of_words[:0] = string
    return list_of_words


def wisielec(number_of_try):
    a = ['W', 'I', 'S', 'I', 'E', 'L', 'E', 'C']
    b = '-'.join(a[0:number_of_try])
    while number_of_try != 8:
        tip_false.configure(text=f'Odliczamy: {b}')
        return
    tip_false.configure(text=f'PRZEGRANA!\n Rozwiązanie: {random_word}\n')
    return


def check_answer():
    global counter
    global answers
    list_a = convert(random_word)
    letter_to_check = check_letter.get()
    if letter_to_check in list_a:
        for i in list_a:
            if letter_to_check == i:
                answers += letter_to_check
        tip_true.configure(text=f'Te litery znajdują się w rozwiązaniu: {answers}')
        tip_label.configure(text=f'Odkryte litery:  {label_tip()}')
        return
    else:
        counter += 1
        return wisielec(counter)


def label_tip():
    list_a = convert(random_word)
    label_list = list(len(list_a) * 'X')
    temp_list_a = list_a
    for i in answers:
        for n in temp_list_a:
            if i == n:
                index = temp_list_a.index(n)
                label_list[index] = i
                temp_list_a[index] = None
    return label_list


window = tk.Tk()
window.geometry('500x300')
window.title('Wisielec')

main_label = tk.Label(window, height=8,
                      text='Witaj w grze, zgadnij jakie litery są w wylosowanym słowie i nie daj się powiesić!')
main_label.pack()

# button1 = tk.Button(window, padx=5, pady=3, text="Losuj słowo", command=get_word())
# button1.pack()

check_letter = tk.Entry(width=20)
check_letter.insert(0, 'Podaj litere')
check_letter.pack()

button2 = tk.Button(window, padx=5, pady=3, text="Sprawdźmy!", command=check_answer)
button2.pack()

tip_false = tk.Label(window, text='')
tip_false.pack()

tip_true = tk.Label(window, text='')
tip_true.pack()

tip_label = tk.Label(window, text='')
tip_label.pack()

window.mainloop()
