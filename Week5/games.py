import tkinter as tk
from tkinter import messagebox
from random import randint


def guess_number():
    diff = abs(target - int(check_number.get()))
    if diff == 0:
        tip.configure(text=f'Koniec, Wygrałeś!, Twój wynik to {len(guesses)}')
        return
    guesses.append(diff)
    if len(guesses) == 1:
        return

    if guesses[-1] > guesses[-2]:
        tip.configure(text='Zimnoo..')
    if guesses[-1] < guesses[-2]:
        tip.configure(text='Cieplej!')
    if guesses[-1] == guesses[-2]:
        tip.configure(text='uaa..')


target = randint(1, 50)
print(target)
guesses = []

window = tk.Tk()
window.geometry('500x500')
window.title("Zagrajmy!")

label = tk.Label(window, text='Zgadnij jaką liczbę mam na myśli!')
label.pack()

check_number = tk.Entry()
check_number.pack()

button = tk.Button(text='Zgaduję!', command=guess_number)
button.pack()

tip = tk.Label(window, text='')
tip.pack()

window.mainloop()
