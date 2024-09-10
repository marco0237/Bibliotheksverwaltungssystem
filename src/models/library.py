from typing import List  # Typing concept in python
from models.book import Book
from models.member import Member


class Library:
    # Initialisierungsmethode Konstruktor
    def __init__(self):
        # self.books = List[Book] # Public Attribut books
        # self.members = List[Member] #Attribut members
        self.books = []  # Public Attribut books
        self.members = list()  # Attribut members

    # Methoden
    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"Buch '{book.title}' wurde entfernt")
        else:
            print(f"buch'{book.title}' ist nicht in der Bibiothek")

    def register_member(self, member):
        self.members.append(member)
        print(f"Der neuen Miglied heißt'{member.name}'")

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        print(f"es existiert kein Buch mit'{isbn}'")

    def list_available_books(self):
        pass

    def list_borrowed_books(self):
        pass
