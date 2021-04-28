from json import load, dump

choice = input(f'[w]ypisz książki\n[d]odaj książkę\nWybierz co chcesz zrobić: ')
books = []
with open('sample.json') as data:
    books = load(data)
    if choice == 'w':
        print(f' Nazwa: {books["name"]}')
        print(f'Pozycje: ')
        for book in books["positions"]:
            print(f'- Tytuł: {book["title"]}, Autor: {book["author"]}')

    elif choice == 'd':
        title = input('Podaj tytuł książki: ')
        author_name = input('Podaj imię i nazwisko autora: ')
        books["positions"].append({
            "id": len(books["positions"]) + 1,
            "title": author_name,
            "author": title
        })
        with open('sample.json', 'w') as data:
            dump(books, data)
    else:
        print('Nie rozumiem polecenia')
