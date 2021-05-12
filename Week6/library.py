from datetime import datetime


class Author:
    def __init__(self, first_name: str, last_name: str, day_of_birth: str):
        self.first_name = first_name
        self.last_name = last_name
        self.day_of_birth = day_of_birth


class Book:
    def __init__(self, title, genre, authors, description, book_summary, rating):
        self.title = title
        self.genre = genre
        self.authors = authors
        self.description = description
        self.book_summary = book_summary
        self.rating = rating


Bonifacy = Author('Bonifacy', 'Smith', datetime(1910, 10, 10))
john = Author('John', 'Smith', datetime(1920, 4, 2))

book = Book(
    'Przykładowy tytuł',
    'Kryminał',
    [Bonifacy, john],
    ...
)
