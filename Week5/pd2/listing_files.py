from json import dump
from os import listdir

list_of_files = listdir('C:/Users/Kuba/PycharmProjects/Pystart/Week5/')
list_of_txt = []

print(list_of_files)

for i in list_of_files:
    if '.txt' in i:
        list_of_txt.append(i)

with open('scalone.txt', 'w') as scalone:
    dump(list_of_txt, scalone)