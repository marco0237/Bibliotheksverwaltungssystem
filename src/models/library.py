from models.book import Book
# TDD(test drive develop)


class Library:
    # initialise constructor
    def __init__(self):
        # self.books = List[Book] # Public Attribute books
        # self.members = List[Member] # Attribut members
        self.books = []  # Public Attribute books
        self.members = list()  # Attribute members

    # Methode
    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            return True
        else:
            return False

    def register_member(self, member):
        self.members.append(member)
        return True

    def find_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
            else:
                return False

    def list_available_books(self):
        # Auflisten alle available book
        available_books = []
        for book in self.books:
            if book.available:
                available_books.append(book)
        return available_books

    def list_borrowed_books(self):
        borrowed_books = []
        for book in self.books:
            if not book.available:
                borrowed_books.append(book)
        return borrowed_books
