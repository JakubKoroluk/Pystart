import sqlite3


def get_books(c):
    return c.execute('SELECT book_id, title, author FROM books')


def save_book(con, t, a):
    c = con.cursor()
    c.execute('INSERT INTO books(title, author) VALUES(?, ?)', (t, a))
    con.commit()


action = input('Co chcesz robić? W-wyświetl, D-dodaj: ')

if action == 'w':
    with sqlite3.connect('library.db') as connection:
        cursor = connection.cursor()
        for book in get_books(cursor):
            book_id, title, author = book
            print(f'id: {book_id}, tytuł: {title}, autor: {author}')
elif action == 'd':
    with sqlite3.connect('library.db') as connection:
        title = input('Podaj tytuł: ')
        author = input('Podaj autora: ')
        save_book(connection, title, author)




else:
    print('Nie wiem o co chodzi..')
